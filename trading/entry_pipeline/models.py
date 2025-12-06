# ============================================
# 📦 DATA MODELS FOR ENTRY PIPELINE
# Dataclasses cho Entry Pipeline
# ============================================

from dataclasses import dataclass, field
from typing import Optional, Dict, List, Any
from enum import Enum


class SignalDirection(Enum):
    """Direction of trading signal"""
    LONG = "LONG"
    SHORT = "SHORT"
    NEUTRAL = "NEUTRAL"
    HOLD = "HOLD"


@dataclass
class MLPrediction:
    """Result from ML Ensemble prediction"""
    direction: SignalDirection
    confidence: float  # 0-1
    individual_predictions: Dict[str, float] = field(default_factory=dict)
    model_agreement: float = 0.0  # 0-1, higher = more agreement
    
    @property
    def is_valid(self) -> bool:
        """Check if prediction is actionable"""
        return self.direction in [SignalDirection.LONG, SignalDirection.SHORT] and self.confidence > 0.5


@dataclass
class PriceActionResult:
    """Result from Price Action Validation"""
    passed: bool
    score: int  # 0-8
    max_score: int = 8
    details: Dict[str, Any] = field(default_factory=dict)
    
    # Individual scores
    candlestick_score: int = 0  # 0-2
    sr_proximity_score: int = 0  # 0-2
    volume_score: int = 0  # 0-1
    candle_direction_score: int = 0  # 0-1
    divergence_score: int = 0  # 0-1
    structure_score: int = 0  # 0-1
    
    # Patterns detected
    patterns_detected: List[str] = field(default_factory=list)
    nearest_support: Optional[float] = None
    nearest_resistance: Optional[float] = None


@dataclass
class StageResult:
    """Result from a single pipeline stage"""
    stage_name: str
    passed: bool
    score: Optional[float] = None
    max_score: Optional[float] = None
    reason: str = ""
    details: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def score_pct(self) -> Optional[float]:
        if self.score is not None and self.max_score and self.max_score > 0:
            return (self.score / self.max_score) * 100
        return None


@dataclass
class EntryDecision:
    """Final decision from Entry Pipeline"""
    should_enter: bool
    direction: SignalDirection = SignalDirection.HOLD
    confidence: float = 0.0  # 0-1

    # Entry details
    entry_price: Optional[float] = None
    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None

    # Stage tracking
    stages_passed: List[str] = field(default_factory=list)
    stages_failed: List[str] = field(default_factory=list)
    stage_results: List['StageResult'] = field(default_factory=list)

    # Reason for decision
    reason: str = ""

    # Additional metadata
    symbol: str = ""
    timestamp: Optional[float] = None
    processing_time_ms: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for logging/serialization"""
        return {
            "should_enter": self.should_enter,
            "direction": self.direction.value,
            "confidence": round(self.confidence, 4),
            "entry_price": self.entry_price,
            "stop_loss": self.stop_loss,
            "take_profit": self.take_profit,
            "stages_passed": self.stages_passed,
            "stages_failed": self.stages_failed,
            "reason": self.reason,
            "symbol": self.symbol,
            "processing_time_ms": round(self.processing_time_ms, 2),
            "stages": [
                {
                    "name": s.stage_name,
                    "passed": s.passed,
                    "score": s.score,
                    "max_score": s.max_score,
                    "reason": s.reason
                }
                for s in self.stage_results
            ]
        }

    def get_summary(self) -> str:
        """Get a human-readable summary"""
        if self.should_enter:
            entry_str = f"Entry: ${self.entry_price:.4f}" if self.entry_price else ""
            return (
                f"✅ ENTER {self.direction.value} | "
                f"Confidence: {self.confidence*100:.1f}% | "
                f"{entry_str}"
            )
        else:
            failed = ", ".join(self.stages_failed) if self.stages_failed else "N/A"
            return (
                f"❌ SKIP | Failed: {failed} | "
                f"Reason: {self.reason}"
            )


@dataclass
class AIAnalysisResult:
    """Result from AI Quick Check (Stage 5)"""
    decision: str  # "ENTER" or "SKIP"
    confidence: int  # 0-100
    reason: str = ""
    suggested_adjustments: Dict[str, float] = field(default_factory=dict)
    raw_response: Optional[str] = None
    error: Optional[str] = None
    
    @property
    def should_enter(self) -> bool:
        return self.decision.upper() == "ENTER"

