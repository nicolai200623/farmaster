#!/usr/bin/env python3
# ============================================
# 🧪 TEST AI VALIDATOR
# Test script for AI Validator functionality
# ============================================

import os
import sys

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from trading.ai_validator import AIValidator, AIAccuracyTracker
from config import Config
from utils.logger import logger


def test_ai_validator():
    """Test AI Validator with sample data"""

    logger.info("=" * 60)
    logger.info("🧪 TESTING AI VALIDATOR")
    logger.info("=" * 60)

    # Check if API keys are configured
    providers = {
        'claude': Config.ANTHROPIC_API_KEY,
        'grok': Config.XAI_API_KEY,
        'openai': Config.OPENAI_API_KEY,
        'gemini': Config.GOOGLE_API_KEY
    }

    available_providers = [p for p, key in providers.items() if key]

    if not available_providers:
        logger.warning("⚠️ No AI API keys configured!")
        logger.info("   Set one of these environment variables:")
        logger.info("   - ANTHROPIC_API_KEY (for Claude)")
        logger.info("   - XAI_API_KEY (for Grok)")
        logger.info("   - OPENAI_API_KEY (for GPT)")
        logger.info("   - GOOGLE_API_KEY (for Gemini)")
        return

    logger.info(f"✅ Available providers: {', '.join(available_providers)}")

    # Test each available provider
    for provider in available_providers:
        test_provider(provider)

    # Test AI Accuracy Tracker
    test_accuracy_tracker()


def test_provider(provider: str):
    """Test a specific AI provider"""
    logger.info("")
    logger.info("=" * 60)
    logger.info(f"Testing {provider.upper()} provider")
    logger.info("=" * 60)

    try:
        # Initialize validator
        validator = AIValidator(
            provider=provider,
            timeout=10,
            max_retries=1
        )

        # Sample signal data
        symbol = "DOTUSDT"
        signal = "SHORT"
        score = 13
        reasons = [
            "Perfect alignment: All TFs DOWN",
            "Perfect pullback to EMA21",
            "At swing low (support)",
            "RSI neutral (good for entry)",
            "London session (high liquidity)"
        ]

        price_data = {
            'current': 6.234,
            'ema21': 6.240,
            'ema50': 6.350
        }

        indicators = {
            'rsi': 45.2,
            'volume_ratio': 1.8,
            'ml_prob': 0.35  # Bearish
        }

        filters_status = {
            'cooldown': 'PASS',
            'htf_alignment': 'PASS',
            'ml_conviction': 'WEAK'
        }

        logger.info(f"\n📊 Test Signal:")
        logger.info(f"   Symbol: {symbol}")
        logger.info(f"   Direction: {signal}")
        logger.info(f"   Score: {score}/15")
        logger.info(f"   Reasons: {reasons[0]}")

        # Validate signal
        logger.info(f"\n🤖 Calling {provider.upper()} API...")
        approved, reasoning, confidence = validator.validate_signal(
            symbol=symbol,
            signal=signal,
            score=score,
            reasons=reasons,
            price_data=price_data,
            indicators=indicators,
            filters_status=filters_status
        )

        logger.info(f"\n✅ AI Response:")
        logger.info(f"   Decision: {'APPROVE ✅' if approved else 'REJECT ❌'}")
        logger.info(f"   Confidence: {confidence*100:.0f}%")
        logger.info(f"   Reasoning: {reasoning}")

    except Exception as e:
        logger.error(f"❌ Test failed for {provider}: {e}")
        import traceback
        logger.error(traceback.format_exc())


def test_accuracy_tracker():
    """Test AI Accuracy Tracker"""
    logger.info("")
    logger.info("=" * 60)
    logger.info("Testing AI Accuracy Tracker")
    logger.info("=" * 60)

    try:
        # Initialize tracker
        tracker = AIAccuracyTracker(log_file='logs/ai_test_history.json')

        # Record some sample decisions
        logger.info("\n📝 Recording sample decisions...")

        decision_id_1 = tracker.record_decision(
            symbol='BTCUSDT',
            signal='LONG',
            ai_approved=True,
            ai_confidence=0.85,
            ai_reasoning='Strong bullish setup with volume confirmation',
            score=12,
            entry_price=45000.0
        )
        logger.info(f"   Recorded: {decision_id_1}")

        decision_id_2 = tracker.record_decision(
            symbol='ETHUSDT',
            signal='SHORT',
            ai_approved=False,
            ai_confidence=0.45,
            ai_reasoning='Weak setup, potential fake breakdown',
            score=8,
            entry_price=None  # Not entered
        )
        logger.info(f"   Recorded: {decision_id_2}")

        # Simulate trade outcome
        logger.info("\n📊 Updating outcomes...")
        tracker.update_outcome(
            decision_id=decision_id_1,
            outcome='WIN',
            pnl_pct=0.025  # 2.5% profit
        )
        logger.info(f"   Updated: {decision_id_1} -> WIN (+2.5%)")

        # Print statistics
        logger.info("")
        tracker.print_statistics()

        logger.info(f"\n💾 History saved to: {tracker.log_file}")

    except Exception as e:
        logger.error(f"❌ Tracker test failed: {e}")
        import traceback
        logger.error(traceback.format_exc())


def main():
    """Main test function"""
    test_ai_validator()

    logger.info("")
    logger.info("=" * 60)
    logger.info("✅ AI VALIDATOR TEST COMPLETE")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
