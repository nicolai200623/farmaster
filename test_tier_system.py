#!/usr/bin/env python3
"""
Test script to verify 2-tier system configuration
"""

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from config import Config
from utils.logger import logger

def main():
    """Test tier system configuration"""
    print("=" * 60)
    print("🧪 TESTING 2-TIER SYSTEM CONFIGURATION")
    print("=" * 60)

    # Check Entry Pipeline config
    print("\n📋 Entry Pipeline Configuration:")
    print(f"   USE_ENTRY_PIPELINE: {Config.USE_ENTRY_PIPELINE}")
    print(f"   USE_ML_ENSEMBLE: {Config.USE_ML_ENSEMBLE}")
    print(f"   ML_CONFIDENCE_THRESHOLD: {Config.ML_CONFIDENCE_THRESHOLD}")
    print(f"   ML_NEUTRAL_ZONE: {Config.ML_NEUTRAL_ZONE}")

    # Check AI configuration
    print("\n🤖 AI Configuration:")
    print(f"   USE_AI_CHECK: {Config.USE_AI_CHECK}")
    print(f"   AI_PROVIDER: {Config.AI_PROVIDER}")
    print(f"   AI_VALIDATOR_MODE: {Config.AI_VALIDATOR_MODE}")
    print(f"   AI_CHECK_BORDERLINE_ONLY: {Config.AI_CHECK_BORDERLINE_ONLY}")
    print(f"   GROK_MODEL: {Config.GROK_MODEL}")

    # Check API key
    xai_key = Config.XAI_API_KEY
    if xai_key:
        print(f"   XAI_API_KEY: {xai_key[:20]}... (length: {len(xai_key)})")
    else:
        print("   ⚠️ XAI_API_KEY: NOT SET")

    # Check Ensemble config
    print("\n🎭 Ensemble Configuration:")
    print(f"   USE_ENSEMBLE: {Config.USE_ENSEMBLE}")
    print(f"   ENSEMBLE_MODELS: {Config.ENSEMBLE_MODELS}")
    print(f"   ENSEMBLE_WEIGHTS: {Config.ENSEMBLE_WEIGHTS}")

    # Check SmartEntry config
    print("\n🎯 Smart Entry Configuration:")
    print(f"   USE_SMART_ENTRY_V2: {Config.USE_SMART_ENTRY_V2}")
    print(f"   MIN_ENTRY_SCORE: {Config.MIN_ENTRY_SCORE}")

    # Verify 2-tier system is properly configured
    print("\n✅ Verification:")

    errors = []
    warnings = []

    if not Config.USE_ENTRY_PIPELINE:
        errors.append("❌ USE_ENTRY_PIPELINE is False - Entry Pipeline disabled!")
    else:
        print("   ✓ Entry Pipeline enabled")

    if not Config.USE_ML_ENSEMBLE:
        errors.append("❌ USE_ML_ENSEMBLE is False - Tier 1 (ML models) disabled!")
    else:
        print("   ✓ Tier 1 (ML Ensemble) enabled")

    if not Config.USE_AI_CHECK:
        errors.append("❌ USE_AI_CHECK is False - Tier 2 (AI) disabled!")
    else:
        print("   ✓ Tier 2 (AI Analyzer) enabled")

    if Config.AI_VALIDATOR_MODE == 'all':
        print("   ℹ️ AI will analyze ALL signals (mode='all')")
    elif Config.AI_VALIDATOR_MODE == 'borderline':
        print("   ℹ️ AI will analyze BORDERLINE signals only (mode='borderline')")
    else:
        print(f"   ℹ️ AI mode: {Config.AI_VALIDATOR_MODE}")

    if not Config.XAI_API_KEY:
        warnings.append("⚠️ XAI_API_KEY not set - AI Analyzer will not work!")
    else:
        print("   ✓ Grok API key configured")

    if not Config.USE_ENSEMBLE:
        warnings.append("⚠️ USE_ENSEMBLE is False - Using single LSTM model")
    else:
        print("   ✓ Ensemble models enabled")

    # Print summary
    print("\n" + "=" * 60)
    if errors:
        print("🔴 ERRORS FOUND:")
        for error in errors:
            print(f"   {error}")

    if warnings:
        print("\n🟡 WARNINGS:")
        for warning in warnings:
            print(f"   {warning}")

    if not errors and not warnings:
        print("✅ ALL CHECKS PASSED - 2-Tier system properly configured!")
    elif not errors:
        print("✅ Configuration valid (with warnings)")
    else:
        print("❌ Configuration has errors - please fix .env file")

    print("=" * 60)

    # Return exit code
    return 0 if not errors else 1


if __name__ == '__main__':
    exit(main())
