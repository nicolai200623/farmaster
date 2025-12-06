# ============================================
# 🤖 AI VALIDATOR
# AI-powered signal validation using Grok/Claude
# ============================================

import os
import json
import time
from typing import Dict, Tuple, Optional, List
from datetime import datetime
import requests
from anthropic import Anthropic

from utils.logger import logger


class AIValidator:
    """
    AI Validator for trading signals using Grok (xAI) or Claude (Anthropic)

    Provides intelligent signal validation by analyzing:
    - Technical setup quality
    - Market context
    - Risk/Reward assessment
    - Potential traps (liquidity sweeps, stop hunts)
    """

    def __init__(
        self,
        provider: str = 'claude',  # 'grok' or 'claude'
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        timeout: int = 5,
        max_retries: int = 2
    ):
        """
        Initialize AI Validator

        Args:
            provider: 'grok' or 'claude'
            api_key: API key (if None, read from env)
            model: Model name (if None, use default)
            timeout: Request timeout in seconds
            max_retries: Max retry attempts
        """
        self.provider = provider.lower()
        self.timeout = timeout
        self.max_retries = max_retries

        # Setup API
        if self.provider == 'grok':
            self.api_key = api_key or os.getenv('GROK_API_KEY', '')
            self.model = model or os.getenv('GROK_MODEL', 'grok-beta')
            self.api_url = 'https://api.x.ai/v1/chat/completions'
        elif self.provider == 'claude':
            self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY', '')
            self.model = model or os.getenv('CLAUDE_MODEL', 'claude-3-haiku-20240307')
            self.client = Anthropic(api_key=self.api_key) if self.api_key else None
        else:
            raise ValueError(f"Unknown provider: {provider}. Use 'grok' or 'claude'")

        if not self.api_key:
            logger.warning(f"⚠️ AI Validator: No API key found for {provider}")

        logger.info(f"🤖 AI Validator initialized: {provider} ({self.model})")

    def validate_signal(
        self,
        symbol: str,
        signal: str,
        score: int,
        reasons: List[str],
        price_data: Dict,
        indicators: Dict,
        filters_status: Dict
    ) -> Tuple[bool, str, float]:
        """
        Validate trading signal using AI

        Args:
            symbol: Trading symbol
            signal: 'LONG' or 'SHORT'
            score: Smart entry score (0-15)
            reasons: List of entry reasons
            price_data: Price information (current, ema21, ema50, etc)
            indicators: Technical indicators (rsi, volume, etc)
            filters_status: Status of various filters

        Returns:
            Tuple of (approved: bool, reasoning: str, confidence: float)
        """
        if not self.api_key:
            logger.debug("AI Validator disabled (no API key)")
            return True, "AI validator not configured", 0.5

        try:
            # Build prompt
            prompt = self._build_prompt(
                symbol, signal, score, reasons,
                price_data, indicators, filters_status
            )

            # Call AI
            for attempt in range(self.max_retries):
                try:
                    if self.provider == 'grok':
                        response = self._call_grok(prompt)
                    else:
                        response = self._call_claude(prompt)

                    # Parse response
                    approved, reasoning, confidence = self._parse_response(response)

                    logger.info(f"🤖 AI Decision: {'APPROVE' if approved else 'REJECT'} ({confidence:.0%} confident)")
                    logger.info(f"   Reasoning: {reasoning}")

                    return approved, reasoning, confidence

                except Exception as e:
                    if attempt < self.max_retries - 1:
                        logger.warning(f"AI call failed (attempt {attempt+1}/{self.max_retries}): {e}")
                        time.sleep(1)
                    else:
                        raise

        except Exception as e:
            logger.error(f"AI Validator error: {e}")
            # Fallback: approve if score is high
            fallback_approve = score >= 10
            return fallback_approve, f"AI error (fallback: {fallback_approve})", 0.5

    def _build_prompt(
        self,
        symbol: str,
        signal: str,
        score: int,
        reasons: List[str],
        price_data: Dict,
        indicators: Dict,
        filters_status: Dict
    ) -> str:
        """Build AI prompt with trading context"""

        # Format reasons
        reasons_text = "\n".join(f"- {r}" for r in reasons[:5])

        # Format filters
        filters_text = "\n".join(f"- {k}: {v}" for k, v in filters_status.items())

        prompt = f"""You are an expert crypto trading analyst. Evaluate this {signal} signal for {symbol}.

SIGNAL STRENGTH: {score}/15 ({"Very Strong" if score >= 10 else "Strong" if score >= 7 else "Moderate"})

ENTRY REASONS:
{reasons_text}

TECHNICAL DATA:
- Current Price: ${price_data.get('current', 0):.4f}
- EMA21: ${price_data.get('ema21', 0):.4f}
- EMA50: ${price_data.get('ema50', 0):.4f}
- RSI: {indicators.get('rsi', 0):.1f}
- Volume Ratio: {indicators.get('volume_ratio', 1):.2f}x
- ML Prediction: {indicators.get('ml_prob', 0.5):.3f}

FILTERS STATUS:
{filters_text}

TASK: Should we enter this {signal} trade?

Consider:
1. Technical setup quality (is this a clean entry?)
2. Risk/Reward ratio (is R:R favorable?)
3. Market traps (liquidity sweeps, stop hunts, fake breakouts?)
4. Timing (is this good market timing?)

IMPORTANT:
- If score >= 10 and filters pass: Likely APPROVE
- If score 7-9: Use your judgment
- If any red flags (traps, bad timing): REJECT
- Be concise (1-2 sentences max)

Respond in this EXACT format:
DECISION: [APPROVE/REJECT]
CONFIDENCE: [0-100]%
REASONING: [Your 1-2 sentence analysis]"""

        return prompt

    def _call_grok(self, prompt: str) -> str:
        """Call Grok API (xAI)"""
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        payload = {
            'model': self.model,
            'messages': [
                {
                    'role': 'system',
                    'content': 'You are a professional crypto trading analyst. Be concise and decisive.'
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            'temperature': 0.3,  # Low temperature for consistent analysis
            'max_tokens': 150
        }

        response = requests.post(
            self.api_url,
            headers=headers,
            json=payload,
            timeout=self.timeout
        )
        response.raise_for_status()

        result = response.json()
        return result['choices'][0]['message']['content']

    def _call_claude(self, prompt: str) -> str:
        """Call Claude API (Anthropic)"""
        if not self.client:
            raise RuntimeError("Claude client not initialized (missing API key)")

        message = self.client.messages.create(
            model=self.model,
            max_tokens=150,
            temperature=0.3,
            system="You are a professional crypto trading analyst. Be concise and decisive.",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return message.content[0].text

    def _parse_response(self, response: str) -> Tuple[bool, str, float]:
        """
        Parse AI response

        Returns:
            Tuple of (approved, reasoning, confidence)
        """
        lines = response.strip().split('\n')

        decision = None
        confidence = 0.5
        reasoning = ""

        for line in lines:
            line = line.strip()

            if line.startswith('DECISION:'):
                decision_text = line.split(':', 1)[1].strip().upper()
                decision = 'APPROVE' in decision_text

            elif line.startswith('CONFIDENCE:'):
                conf_text = line.split(':', 1)[1].strip()
                # Extract number (handle formats like "75%", "75", "0.75")
                conf_text = conf_text.replace('%', '').strip()
                try:
                    conf_val = float(conf_text)
                    confidence = conf_val / 100 if conf_val > 1 else conf_val
                except:
                    confidence = 0.5

            elif line.startswith('REASONING:'):
                reasoning = line.split(':', 1)[1].strip()

        # Fallback if parsing failed
        if decision is None:
            # Simple keyword detection
            response_upper = response.upper()
            if 'APPROVE' in response_upper or 'YES' in response_upper or 'ENTER' in response_upper:
                decision = True
            elif 'REJECT' in response_upper or 'NO' in response_upper or 'AVOID' in response_upper:
                decision = False
            else:
                decision = True  # Default to approve if unclear

            reasoning = response[:200] if not reasoning else reasoning

        return decision, reasoning, confidence


class AIAccuracyTracker:
    """
    Track AI validator accuracy over time

    Records AI decisions and actual trade outcomes to measure performance
    """

    def __init__(self, log_file: str = 'logs/ai_validator_history.json'):
        """
        Initialize tracker

        Args:
            log_file: Path to JSON log file
        """
        self.log_file = log_file
        self.decisions = []

        # Create logs directory if needed
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Load existing history
        self._load_history()

    def _load_history(self):
        """Load decision history from file"""
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, 'r') as f:
                    self.decisions = json.load(f)
                logger.info(f"📊 Loaded {len(self.decisions)} AI decisions from history")
            except Exception as e:
                logger.warning(f"Could not load AI history: {e}")
                self.decisions = []

    def _save_history(self):
        """Save decision history to file"""
        try:
            with open(self.log_file, 'w') as f:
                json.dump(self.decisions, f, indent=2)
        except Exception as e:
            logger.error(f"Could not save AI history: {e}")

    def record_decision(
        self,
        symbol: str,
        signal: str,
        ai_approved: bool,
        ai_confidence: float,
        ai_reasoning: str,
        score: int,
        entry_price: Optional[float] = None
    ) -> str:
        """
        Record AI decision

        Args:
            symbol: Trading symbol
            signal: 'LONG' or 'SHORT'
            ai_approved: AI decision
            ai_confidence: AI confidence (0-1)
            ai_reasoning: AI reasoning
            score: Entry score
            entry_price: Entry price (if trade was taken)

        Returns:
            decision_id: Unique ID for this decision
        """
        decision_id = f"{symbol}_{int(time.time())}"

        decision = {
            'id': decision_id,
            'timestamp': datetime.now().isoformat(),
            'symbol': symbol,
            'signal': signal,
            'ai_approved': ai_approved,
            'ai_confidence': ai_confidence,
            'ai_reasoning': ai_reasoning,
            'score': score,
            'entry_price': entry_price,
            'outcome': None,  # Will be updated when trade closes
            'outcome_pnl': None
        }

        self.decisions.append(decision)
        self._save_history()

        return decision_id

    def update_outcome(
        self,
        decision_id: str,
        outcome: str,
        pnl_pct: float
    ):
        """
        Update trade outcome

        Args:
            decision_id: Decision ID from record_decision()
            outcome: 'WIN' or 'LOSS'
            pnl_pct: PnL percentage
        """
        for decision in self.decisions:
            if decision['id'] == decision_id:
                decision['outcome'] = outcome
                decision['outcome_pnl'] = pnl_pct
                decision['outcome_timestamp'] = datetime.now().isoformat()
                self._save_history()
                logger.info(f"📊 Updated AI decision {decision_id}: {outcome} ({pnl_pct*100:+.2f}%)")
                return

        logger.warning(f"Decision ID not found: {decision_id}")

    def get_statistics(self, last_n: Optional[int] = None) -> Dict:
        """
        Get AI validator statistics

        Args:
            last_n: Only consider last N decisions (None = all)

        Returns:
            Dict with statistics
        """
        # Filter decisions with outcomes
        completed = [d for d in self.decisions if d['outcome'] is not None]

        if last_n:
            completed = completed[-last_n:]

        if not completed:
            return {
                'total_decisions': len(self.decisions),
                'completed_trades': 0,
                'accuracy': 0,
                'avg_confidence': 0,
                'approved_rate': 0
            }

        # Calculate metrics
        total_decisions = len(self.decisions)
        completed_trades = len(completed)

        approved_count = sum(1 for d in self.decisions if d['ai_approved'])
        approved_rate = approved_count / total_decisions if total_decisions > 0 else 0

        correct_predictions = sum(
            1 for d in completed
            if (d['ai_approved'] and d['outcome'] == 'WIN') or
               (not d['ai_approved'] and d['outcome'] == 'LOSS')
        )
        accuracy = correct_predictions / completed_trades if completed_trades > 0 else 0

        avg_confidence = sum(d['ai_confidence'] for d in completed) / completed_trades

        # Wins when AI approved
        ai_approved_trades = [d for d in completed if d['ai_approved']]
        ai_approved_wins = sum(1 for d in ai_approved_trades if d['outcome'] == 'WIN')
        ai_approved_winrate = ai_approved_wins / len(ai_approved_trades) if ai_approved_trades else 0

        return {
            'total_decisions': total_decisions,
            'completed_trades': completed_trades,
            'accuracy': accuracy,
            'avg_confidence': avg_confidence,
            'approved_rate': approved_rate,
            'ai_approved_trades': len(ai_approved_trades),
            'ai_approved_winrate': ai_approved_winrate
        }

    def print_statistics(self, last_n: Optional[int] = None):
        """Print statistics to logger"""
        stats = self.get_statistics(last_n)

        logger.info("=" * 60)
        logger.info("🤖 AI VALIDATOR STATISTICS")
        if last_n:
            logger.info(f"   (Last {last_n} decisions)")
        logger.info("=" * 60)
        logger.info(f"Total Decisions: {stats['total_decisions']}")
        logger.info(f"Completed Trades: {stats['completed_trades']}")
        logger.info(f"AI Accuracy: {stats['accuracy']*100:.1f}%")
        logger.info(f"Avg Confidence: {stats['avg_confidence']*100:.1f}%")
        logger.info(f"Approval Rate: {stats['approved_rate']*100:.1f}%")
        logger.info(f"AI-Approved Win Rate: {stats['ai_approved_winrate']*100:.1f}%")
        logger.info("=" * 60)
