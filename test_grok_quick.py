#!/usr/bin/env python3
"""
Quick test for Grok AI integration
"""
import os
import sys
from openai import OpenAI

# Load from environment variable or .env file
from dotenv import load_dotenv
load_dotenv()

XAI_API_KEY = os.getenv('XAI_API_KEY', '')

if not XAI_API_KEY:
    print("ERROR: XAI_API_KEY not found in environment!")
    print("Please set it in .env file or export XAI_API_KEY=your_key")
    sys.exit(1)

print("=" * 60)
print("TESTING GROK AI CONNECTION")
print("=" * 60)

try:
    # Initialize Grok client (uses OpenAI-compatible API)
    client = OpenAI(
        api_key=XAI_API_KEY,
        base_url="https://api.x.ai/v1"
    )

    print("\nGrok client initialized")
    print(f"   API Key: {XAI_API_KEY[:20]}...")

    # Send test request
    print("\nSending test request to Grok...")
    response = client.chat.completions.create(
        model="grok-2-latest",
        messages=[
            {
                "role": "system",
                "content": "You are a trading signal validator. Respond in JSON format only."
            },
            {
                "role": "user",
                "content": """Analyze this LONG signal for BTCUSDT:
- ML Confidence: 0.72
- Entry Score: 12/15
- Price Action Score: 7/8
- HTF Trend: Aligned

Should we enter? Respond ONLY with JSON:
{
    "decision": "ENTER" or "SKIP",
    "confidence": 0-100,
    "reason": "Brief explanation"
}"""
            }
        ],
        temperature=0.3,
        max_tokens=256
    )

    result = response.choices[0].message.content

    print("\nGROK AI RESPONSE:")
    print(result)
    print("\n" + "=" * 60)
    print("GROK AI TEST PASSED!")
    print("=" * 60)

except Exception as e:
    print(f"\nERROR: {e}")
    import traceback
    traceback.print_exc()
    print("\n" + "=" * 60)
    print("GROK AI TEST FAILED")
    print("=" * 60)
