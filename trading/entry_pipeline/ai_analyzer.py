# ============================================
# 🤖 STAGE 5: AI QUICK CHECK (OPTIONAL)
# Multi-provider AI integration for borderline cases
# Supports: Claude, Grok, OpenAI, Gemini
# ============================================

import json
import os
from typing import Dict, Optional, Any
from dataclasses import asdict
from abc import ABC, abstractmethod
from enum import Enum

from trading.entry_pipeline.models import (
    SignalDirection,
    StageResult,
    AIAnalysisResult,
    MLPrediction
)
from utils.logger import logger


class AIProvider(Enum):
    """Supported AI providers"""
    CLAUDE = "claude"
    GROK = "grok"
    OPENAI = "openai"
    GEMINI = "gemini"


# ============================================
# AI PROVIDER CLIENTS
# ============================================

# Try importing various AI packages
ANTHROPIC_AVAILABLE = False
OPENAI_AVAILABLE = False
GOOGLE_AVAILABLE = False

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    pass

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    pass

try:
    import google.generativeai as genai
    GOOGLE_AVAILABLE = True
except ImportError:
    pass


class BaseAIClient(ABC):
    """Base class for AI provider clients"""

    @abstractmethod
    def call(self, system_prompt: str, user_prompt: str) -> str:
        """Call the AI API and return response text"""
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Check if this provider is available"""
        pass


class ClaudeClient(BaseAIClient):
    """Anthropic Claude client"""

    def __init__(self, api_key: str, model: str = "claude-3-haiku-20240307"):
        self.api_key = api_key
        self.model = model
        self.client = None
        if ANTHROPIC_AVAILABLE and api_key:
            self.client = anthropic.Anthropic(api_key=api_key)

    def is_available(self) -> bool:
        return ANTHROPIC_AVAILABLE and self.client is not None

    def call(self, system_prompt: str, user_prompt: str) -> str:
        message = self.client.messages.create(
            model=self.model,
            max_tokens=256,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}]
        )
        return message.content[0].text


class GrokClient(BaseAIClient):
    """xAI Grok client (uses OpenAI-compatible API)"""

    def __init__(self, api_key: str, model: str = "grok-2-latest"):
        self.api_key = api_key
        self.model = model
        self.client = None
        if OPENAI_AVAILABLE and api_key:
            self.client = openai.OpenAI(
                api_key=api_key,
                base_url="https://api.x.ai/v1"
            )

    def is_available(self) -> bool:
        return OPENAI_AVAILABLE and self.client is not None

    def call(self, system_prompt: str, user_prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            max_tokens=256,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content


class OpenAIClient(BaseAIClient):
    """OpenAI GPT client"""

    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        self.api_key = api_key
        self.model = model
        self.client = None
        if OPENAI_AVAILABLE and api_key:
            self.client = openai.OpenAI(api_key=api_key)

    def is_available(self) -> bool:
        return OPENAI_AVAILABLE and self.client is not None

    def call(self, system_prompt: str, user_prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            max_tokens=256,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content


class GeminiClient(BaseAIClient):
    """Google Gemini client"""

    def __init__(self, api_key: str, model: str = "gemini-1.5-flash"):
        self.api_key = api_key
        self.model_name = model
        self.model = None
        if GOOGLE_AVAILABLE and api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(model)

    def is_available(self) -> bool:
        return GOOGLE_AVAILABLE and self.model is not None

    def call(self, system_prompt: str, user_prompt: str) -> str:
        # Gemini combines system + user prompt
        full_prompt = f"{system_prompt}\n\n{user_prompt}"
        response = self.model.generate_content(full_prompt)
        return response.text


class AIEntryAnalyzer:
    """
    Stage 5: AI Quick Check for Borderline Cases

    Multi-provider support:
    - Claude (Anthropic) - claude-3-haiku
    - Grok (xAI) - grok-2-latest
    - OpenAI - gpt-4o-mini
    - Gemini (Google) - gemini-1.5-flash

    Only triggers for borderline cases (PA score 5-6)
    Fallback: skip AI check if fails
    """

    # Default models per provider
    DEFAULT_MODELS = {
        AIProvider.CLAUDE: "claude-3-haiku-20240307",
        AIProvider.GROK: "grok-4-1-fast-reasoning",  # Fast reasoning model for crypto trading
        AIProvider.OPENAI: "gpt-4o-mini",
        AIProvider.GEMINI: "gemini-1.5-flash"
    }

    SYSTEM_PROMPT = """You are an expert crypto trading analyst. Analyze the trading setup and provide a quick decision.

You will receive market data including:
- Symbol and timeframe
- ML model predictions
- Entry scores
- Technical indicators
- Recent price action

Respond ONLY with valid JSON in this exact format:
{
    "decision": "ENTER" or "SKIP",
    "confidence": 0-100,
    "reason": "Brief 1-2 sentence explanation",
    "suggested_adjustments": {
        "tp_multiplier": 1.0,
        "sl_multiplier": 1.0
    }
}

Guidelines:
- Be conservative - when in doubt, SKIP
- Consider risk/reward ratio
- Watch for market manipulation patterns
- High volume confirmation is important
- Divergences are warning signs"""

    def __init__(self, config: Dict):
        """
        Initialize AI Entry Analyzer with multi-provider support

        Args:
            config: Configuration dictionary with:
                - USE_AI_CHECK: bool
                - AI_PROVIDER: str (claude, grok, openai, gemini)
                - ANTHROPIC_API_KEY / XAI_API_KEY / OPENAI_API_KEY / GOOGLE_API_KEY
                - AI_MODEL: str (optional, uses default per provider)
        """
        self.config = config
        self.use_ai = config.get('USE_AI_CHECK', False)
        self.use_for_borderline = config.get('AI_CHECK_BORDERLINE_ONLY', True)

        # Determine provider
        provider_str = config.get('AI_PROVIDER', 'claude').lower()
        try:
            self.provider = AIProvider(provider_str)
        except ValueError:
            logger.warning(f"⚠️ Unknown AI provider: {provider_str}, defaulting to claude")
            self.provider = AIProvider.CLAUDE

        # Initialize client based on provider
        self.client = self._init_client()
        self.enabled = self.use_ai and self.client is not None and self.client.is_available()

        if self.enabled:
            logger.info(f"🤖 AIEntryAnalyzer initialized (provider: {self.provider.value})")
        elif self.use_ai:
            logger.warning(f"⚠️ AI Check enabled but {self.provider.value} client not available")

    def _init_client(self) -> Optional[BaseAIClient]:
        """Initialize the appropriate AI client based on provider"""
        model = self.config.get('AI_MODEL', self.DEFAULT_MODELS.get(self.provider))

        if self.provider == AIProvider.CLAUDE:
            api_key = self.config.get('ANTHROPIC_API_KEY', os.getenv('ANTHROPIC_API_KEY', ''))
            return ClaudeClient(api_key, model)

        elif self.provider == AIProvider.GROK:
            api_key = self.config.get('XAI_API_KEY', os.getenv('XAI_API_KEY', ''))
            return GrokClient(api_key, model)

        elif self.provider == AIProvider.OPENAI:
            api_key = self.config.get('OPENAI_API_KEY', os.getenv('OPENAI_API_KEY', ''))
            return OpenAIClient(api_key, model)

        elif self.provider == AIProvider.GEMINI:
            api_key = self.config.get('GOOGLE_API_KEY', os.getenv('GOOGLE_API_KEY', ''))
            return GeminiClient(api_key, model)

        return None
    def should_analyze(self, pa_score: int, entry_score: int = 0) -> bool:
        """
        Check if AI analysis should be triggered

        Args:
            pa_score: Price action score (0-8)
            entry_score: Smart entry score (0-15)

        Returns:
            bool: True if AI should analyze
        """
        if not self.enabled:
            return False

        # Get validator mode from config
        validator_mode = self.config.get('AI_VALIDATOR_MODE', 'borderline')

        if validator_mode == 'all':
            # Analyze all signals
            return True
        elif validator_mode == 'tiebreaker':
            # Only analyze when filters conflict or score borderline
            # For now, use borderline logic
            min_score = self.config.get('AI_MIN_SCORE_FOR_CHECK', 7)
            max_score = self.config.get('AI_MAX_SCORE_FOR_CHECK', 10)
            return min_score <= entry_score <= max_score
        else:  # 'borderline' mode (default)
            if self.use_for_borderline:
                # Original logic: PA score 5-6
                return pa_score in [5, 6]
            else:
                # Use entry score range
                min_score = self.config.get('AI_MIN_SCORE_FOR_CHECK', 7)
                max_score = self.config.get('AI_MAX_SCORE_FOR_CHECK', 10)
                return min_score <= entry_score <= max_score
    
    def analyze(
        self,
        symbol: str,
        ml_prediction: MLPrediction,
        entry_score: int,
        pa_score: int,
        df,  # DataFrame
        technical_summary: Dict[str, Any] = None
    ) -> AIAnalysisResult:
        """
        Analyze entry with AI

        Args:
            symbol: Trading symbol
            ml_prediction: ML prediction result
            entry_score: Smart entry score
            pa_score: Price action score
            df: DataFrame with OHLCV data
            technical_summary: Optional pre-computed summary

        Returns:
            AIAnalysisResult
        """
        logger.info(f"   🤖 [TIER 2] AI Analyzer ({self.provider.value}) analyzing...")
        logger.info(f"      Entry score: {entry_score}/15, PA score: {pa_score}/8")

        if not self.enabled:
            return AIAnalysisResult(
                decision="SKIP",
                confidence=0,
                reason="AI analysis disabled",
                error="Not enabled"
            )
        
        try:
            # Build prompt
            prompt = self._build_prompt(
                symbol, ml_prediction, entry_score, pa_score, df, technical_summary
            )
            
            # Call API with timeout
            response = self._call_api(prompt)
            
            # Parse response
            return self._parse_response(response)
            
        except Exception as e:
            logger.error(f"AI analysis error: {e}")
            return AIAnalysisResult(
                decision="SKIP",
                confidence=0,
                reason="Analysis failed",
                error=str(e)
            )

    def _build_prompt(
        self,
        symbol: str,
        ml_prediction: MLPrediction,
        entry_score: int,
        pa_score: int,
        df,
        technical_summary: Optional[Dict] = None
    ) -> str:
        """Build the analysis prompt"""
        # Get recent candles
        recent = df.tail(10) if len(df) >= 10 else df

        # Build candle summary
        candles = []
        for i, (_, row) in enumerate(recent.iterrows()):
            candles.append({
                'idx': i,
                'o': float(round(row['open'], 2)),
                'h': float(round(row['high'], 2)),
                'l': float(round(row['low'], 2)),
                'c': float(round(row['close'], 2)),
                'v': int(float(row.get('volume', 0)))
            })

        # Build technical summary if not provided
        if technical_summary is None:
            technical_summary = {}
            if 'rsi' in df.columns:
                technical_summary['rsi'] = float(round(df['rsi'].iloc[-1], 2))
            if 'macd' in df.columns:
                technical_summary['macd'] = float(round(df['macd'].iloc[-1], 4))
            if 'atr' in df.columns:
                technical_summary['atr'] = float(round(df['atr'].iloc[-1], 4))

        # Build ML section if available
        ml_section = ""
        if ml_prediction is not None:
            ml_section = f"""
Direction: {ml_prediction.direction.value}
ML Confidence: {ml_prediction.confidence:.2%}
Model Agreement: {ml_prediction.model_agreement:.2%}"""
        else:
            # Detect direction from price action
            direction = "BULLISH" if df['close'].iloc[-1] > df['close'].iloc[-5] else "BEARISH"
            ml_section = f"""
Direction: {direction} (detected from price action)
ML Confidence: N/A (no ML models)
Model Agreement: N/A"""

        prompt = f"""Analyze this trading setup:

Symbol: {symbol}{ml_section}
Entry Score: {entry_score}/15
Price Action Score: {pa_score}/8

Technical Indicators:
{json.dumps(technical_summary, indent=2)}

Recent Candles (oldest to newest):
{json.dumps(candles, indent=2)}

Should we ENTER or SKIP this trade?"""

        return prompt

    def _call_api(self, prompt: str) -> str:
        """Call AI API using configured provider"""
        if not self.client or not self.client.is_available():
            raise ValueError(f"{self.provider.value} client not available")

        return self.client.call(self.SYSTEM_PROMPT, prompt)

    def _parse_response(self, response: str) -> AIAnalysisResult:
        """Parse AI response to AIAnalysisResult"""
        try:
            # Try to extract JSON from response
            response = response.strip()

            # Handle markdown code blocks
            if response.startswith("```"):
                lines = response.split("\n")
                response = "\n".join(lines[1:-1])

            data = json.loads(response)

            return AIAnalysisResult(
                decision=data.get("decision", "SKIP"),
                confidence=data.get("confidence", 0),
                reason=data.get("reason", ""),
                suggested_adjustments=data.get("suggested_adjustments", {})
            )

        except json.JSONDecodeError as e:
            logger.warning(f"Failed to parse AI response: {e}")

            # Try to extract decision from text
            decision = "SKIP"
            if "ENTER" in response.upper():
                decision = "ENTER"

            return AIAnalysisResult(
                decision=decision,
                confidence=50,
                reason=response[:200],
                error="JSON parse failed"
            )

    def to_stage_result(self, ai_result: AIAnalysisResult) -> StageResult:
        """Convert AIAnalysisResult to StageResult"""
        passed = ai_result.decision == "ENTER" and ai_result.confidence >= 60

        return StageResult(
            stage_name="ai_check",
            passed=passed,
            score=ai_result.confidence / 100,
            max_score=1.0,
            reason=f"AI: {ai_result.decision} ({ai_result.confidence}%) - {ai_result.reason}",
            details={
                'decision': ai_result.decision,
                'confidence': ai_result.confidence,
                'reason': ai_result.reason,
                'adjustments': ai_result.suggested_adjustments
            }
        )
