#!/usr/bin/env python3
# ============================================
# ✅ VERIFY GROK MODEL CONFIGURATION
# Quick script to verify grok-4-1-fast-reasoning is configured
# ============================================

import os
import sys

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import Config
from utils.logger import logger


def verify_grok_config():
    """Verify Grok configuration"""

    logger.info("=" * 60)
    logger.info("✅ VERIFYING GROK MODEL CONFIGURATION")
    logger.info("=" * 60)

    # Check AI Validator is enabled
    logger.info("\n1. Checking AI Validator status...")
    if hasattr(Config, 'USE_AI_VALIDATOR'):
        logger.info(f"   USE_AI_VALIDATOR: {Config.USE_AI_VALIDATOR}")
    else:
        logger.warning("   ⚠️ USE_AI_VALIDATOR not found in Config")

    # Check provider
    logger.info("\n2. Checking AI Provider...")
    if hasattr(Config, 'AI_PROVIDER'):
        logger.info(f"   AI_PROVIDER: {Config.AI_PROVIDER}")
        if Config.AI_PROVIDER.lower() == 'grok':
            logger.info("   ✅ Grok provider selected")
        else:
            logger.warning(f"   ⚠️ Using {Config.AI_PROVIDER} instead of Grok")
    else:
        logger.warning("   ⚠️ AI_PROVIDER not found in Config")

    # Check API key
    logger.info("\n3. Checking API Key...")
    xai_key = os.getenv('XAI_API_KEY', '')
    grok_key = os.getenv('GROK_API_KEY', '')

    if xai_key:
        logger.info(f"   XAI_API_KEY: xai-{'*' * 20} (found)")
    if grok_key:
        logger.info(f"   GROK_API_KEY: {'*' * 24} (found)")

    if xai_key or grok_key:
        logger.info("   ✅ API key found")
    else:
        logger.error("   ❌ No API key found!")
        logger.error("   Set XAI_API_KEY or GROK_API_KEY in .env")
        return False

    # Check model
    logger.info("\n4. Checking Model Configuration...")

    # Check environment variable
    env_model = os.getenv('GROK_MODEL', '')
    if env_model:
        logger.info(f"   GROK_MODEL (env): {env_model}")
    else:
        logger.info("   GROK_MODEL (env): Not set (will use default)")

    # Check what model will be used
    from trading.ai_validator import AIValidator

    try:
        validator = AIValidator(provider='grok')
        logger.info(f"   Actual model: {validator.model}")

        if validator.model == 'grok-4-1-fast-reasoning':
            logger.info("   ✅ Using grok-4-1-fast-reasoning (recommended)")
        elif validator.model == 'grok-beta':
            logger.warning("   ⚠️ Using grok-beta (legacy model)")
            logger.warning("   Consider removing GROK_MODEL from .env to use default")
        elif validator.model == 'grok-2-latest':
            logger.warning("   ⚠️ Using grok-2-latest (older model)")
            logger.warning("   Consider removing GROK_MODEL from .env to use default")
        else:
            logger.info(f"   ℹ️ Using custom model: {validator.model}")
    except Exception as e:
        logger.error(f"   ❌ Failed to initialize validator: {e}")
        return False

    # Check AI settings
    logger.info("\n5. Checking AI Validator Settings...")
    if hasattr(Config, 'AI_VALIDATOR_MODE'):
        logger.info(f"   AI_VALIDATOR_MODE: {Config.AI_VALIDATOR_MODE}")
    if hasattr(Config, 'AI_MIN_SCORE_FOR_CHECK'):
        logger.info(f"   AI_MIN_SCORE_FOR_CHECK: {Config.AI_MIN_SCORE_FOR_CHECK}")
    if hasattr(Config, 'AI_MAX_SCORE_FOR_CHECK'):
        logger.info(f"   AI_MAX_SCORE_FOR_CHECK: {Config.AI_MAX_SCORE_FOR_CHECK}")
    if hasattr(Config, 'AI_TIMEOUT_SECONDS'):
        logger.info(f"   AI_TIMEOUT_SECONDS: {Config.AI_TIMEOUT_SECONDS}")
    if hasattr(Config, 'AI_MIN_CONFIDENCE'):
        logger.info(f"   AI_MIN_CONFIDENCE: {Config.AI_MIN_CONFIDENCE}")

    # Summary
    logger.info("\n" + "=" * 60)
    logger.info("📊 CONFIGURATION SUMMARY")
    logger.info("=" * 60)

    summary = []

    # Validator enabled?
    if hasattr(Config, 'USE_AI_VALIDATOR') and Config.USE_AI_VALIDATOR:
        summary.append("✅ AI Validator: ENABLED")
    else:
        summary.append("⚠️ AI Validator: DISABLED")

    # Provider
    if hasattr(Config, 'AI_PROVIDER'):
        if Config.AI_PROVIDER.lower() == 'grok':
            summary.append("✅ Provider: Grok")
        else:
            summary.append(f"⚠️ Provider: {Config.AI_PROVIDER} (not Grok)")

    # API Key
    if xai_key or grok_key:
        summary.append("✅ API Key: Found")
    else:
        summary.append("❌ API Key: Missing")

    # Model
    try:
        validator = AIValidator(provider='grok')
        if validator.model == 'grok-4-1-fast-reasoning':
            summary.append("✅ Model: grok-4-1-fast-reasoning (recommended)")
        else:
            summary.append(f"⚠️ Model: {validator.model}")
    except:
        summary.append("❌ Model: Failed to detect")

    for line in summary:
        logger.info(line)

    # Recommendations
    logger.info("\n" + "=" * 60)
    logger.info("💡 RECOMMENDATIONS")
    logger.info("=" * 60)

    recommendations = []

    if not hasattr(Config, 'USE_AI_VALIDATOR') or not Config.USE_AI_VALIDATOR:
        recommendations.append("Enable AI Validator: Set USE_AI_VALIDATOR=True in .env")

    if hasattr(Config, 'AI_PROVIDER') and Config.AI_PROVIDER.lower() != 'grok':
        recommendations.append(f"Switch to Grok: Set AI_PROVIDER=grok in .env")

    if not (xai_key or grok_key):
        recommendations.append("Add API Key: Set XAI_API_KEY=your-key in .env")

    try:
        validator = AIValidator(provider='grok')
        if validator.model != 'grok-4-1-fast-reasoning':
            recommendations.append("Use latest model: Remove GROK_MODEL from .env (or set to grok-4-1-fast-reasoning)")
    except:
        pass

    if recommendations:
        for i, rec in enumerate(recommendations, 1):
            logger.info(f"{i}. {rec}")
    else:
        logger.info("✅ Configuration is optimal!")

    logger.info("\n" + "=" * 60)

    # Final verdict
    if xai_key or grok_key:
        logger.info("✅ READY TO USE GROK AI VALIDATOR")
        logger.info("\nNext steps:")
        logger.info("1. Run test: python scripts/test_ai_validator.py")
        logger.info("2. Start bot: python bot.py")
        return True
    else:
        logger.error("❌ NOT READY - Missing API key")
        logger.error("\nSetup instructions:")
        logger.error("1. Get API key from https://console.x.ai/")
        logger.error("2. Add to .env: XAI_API_KEY=your-key-here")
        logger.error("3. Run this script again")
        return False


def main():
    """Main function"""
    try:
        success = verify_grok_config()
        sys.exit(0 if success else 1)
    except Exception as e:
        logger.error(f"❌ Verification failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
