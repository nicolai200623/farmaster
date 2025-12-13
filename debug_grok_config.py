#!/usr/bin/env python3
"""
Debug script to check Grok AI configuration
Run this on VPS to diagnose why Grok client is not available
"""
import os
import sys

print("=" * 60)
print("GROK AI CONFIGURATION DEBUG")
print("=" * 60)

# Load config
from config import Config

print("\n1. CHECKING ENVIRONMENT VARIABLES:")
print("-" * 60)
xai_key_env = os.getenv('XAI_API_KEY', '')
print(f"XAI_API_KEY from os.getenv(): '{xai_key_env}'")
print(f"  Length: {len(xai_key_env)}")
print(f"  First 20 chars: '{xai_key_env[:20]}...'")
print(f"  Last 10 chars: '...{xai_key_env[-10:]}'")
print(f"  Is empty: {not bool(xai_key_env)}")
print(f"  Has whitespace: {xai_key_env != xai_key_env.strip()}")

print("\n2. CHECKING CONFIG.PY:")
print("-" * 60)
print(f"Config.XAI_API_KEY: '{Config.XAI_API_KEY}'")
print(f"  Length: {len(Config.XAI_API_KEY)}")
print(f"  First 20 chars: '{Config.XAI_API_KEY[:20]}...'")
print(f"  Is empty: {not bool(Config.XAI_API_KEY)}")

print(f"\nConfig.USE_AI_CHECK: {Config.USE_AI_CHECK}")
print(f"Config.AI_PROVIDER: {Config.AI_PROVIDER}")
print(f"Config.AI_VALIDATOR_MODE: {Config.AI_VALIDATOR_MODE}")
print(f"Config.USE_ENTRY_PIPELINE: {Config.USE_ENTRY_PIPELINE}")

print("\n3. CHECKING OPENAI PACKAGE:")
print("-" * 60)
try:
    import openai
    print(f"✅ openai package installed")
    print(f"   Version: {openai.__version__}")
    OPENAI_AVAILABLE = True
except ImportError as e:
    print(f"❌ openai package NOT available: {e}")
    OPENAI_AVAILABLE = False

print("\n4. TESTING GROK CLIENT INITIALIZATION:")
print("-" * 60)

if OPENAI_AVAILABLE:
    from openai import OpenAI

    if Config.XAI_API_KEY:
        try:
            client = OpenAI(
                api_key=Config.XAI_API_KEY,
                base_url="https://api.x.ai/v1"
            )
            print("✅ Grok client initialized successfully")

            # Test API call
            print("\n5. TESTING GROK API CALL:")
            print("-" * 60)
            response = client.chat.completions.create(
                model="grok-2-latest",
                messages=[
                    {"role": "system", "content": "You are a test assistant."},
                    {"role": "user", "content": "Say 'OK' if you can hear me."}
                ],
                max_tokens=10,
                temperature=0
            )
            result = response.choices[0].message.content
            print(f"✅ Grok API response: {result}")

        except Exception as e:
            print(f"❌ Grok client initialization failed: {e}")
            import traceback
            traceback.print_exc()
    else:
        print("❌ Config.XAI_API_KEY is empty!")
else:
    print("❌ Cannot test Grok client (openai package not available)")

print("\n6. CHECKING ENTRY PIPELINE CONFIG:")
print("-" * 60)

# Simulate what signal_generator does
from trading.signal_generator import SignalGenerator

pipeline_config = {
    'USE_AI_CHECK': getattr(Config, 'USE_AI_CHECK', False),
    'AI_PROVIDER': getattr(Config, 'AI_PROVIDER', 'grok'),
    'XAI_API_KEY': getattr(Config, 'XAI_API_KEY', ''),
    'AI_MODEL': getattr(Config, 'GROK_MODEL', 'grok-2-latest'),
}

print(f"Pipeline config that would be passed to AIEntryAnalyzer:")
for key, value in pipeline_config.items():
    if 'KEY' in key:
        print(f"  {key}: '{value[:20]}...' (length: {len(value)})")
    else:
        print(f"  {key}: {value}")

print("\n7. TESTING AI ANALYZER INITIALIZATION:")
print("-" * 60)

try:
    from trading.entry_pipeline.ai_analyzer import AIEntryAnalyzer

    ai_analyzer = AIEntryAnalyzer(pipeline_config)

    print(f"AIEntryAnalyzer created")
    print(f"  enabled: {ai_analyzer.enabled}")
    print(f"  use_ai: {ai_analyzer.use_ai}")
    print(f"  provider: {ai_analyzer.provider.value}")
    print(f"  client: {ai_analyzer.client}")
    if ai_analyzer.client:
        print(f"  client.is_available(): {ai_analyzer.client.is_available()}")
        print(f"  client.api_key: '{ai_analyzer.client.api_key[:20]}...'")
    else:
        print(f"  ❌ client is None!")

except Exception as e:
    print(f"❌ Error creating AIEntryAnalyzer: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("DEBUG COMPLETE")
print("=" * 60)
