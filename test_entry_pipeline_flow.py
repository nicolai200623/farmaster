#!/usr/bin/env python3
"""
Test Entry Pipeline Flow: ML Ensemble -> Grok AI -> Execute
"""
import os
import sys
import numpy as np
import pandas as pd

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from trading.entry_pipeline import EntryPipeline, SignalDirection
from config import Config
from utils.logger import logger

print("=" * 60)
print("TEST ENTRY PIPELINE FLOW")
print("=" * 60)

# Build config for Entry Pipeline
pipeline_config = {
    # Stage 1: ML Ensemble (DISABLED for testing - will use price direction detection)
    'USE_ML_ENSEMBLE': False,  # Disabled because we don't have trained models in test
    'ML_CONFIDENCE_THRESHOLD': 0.62,
    'ML_NEUTRAL_ZONE': 0.08,

    # Stage 2: Smart Entry (DISABLED)
    'USE_SMART_ENTRY': False,  # DISABLED - only use ML + Grok AI
    'MIN_ENTRY_SCORE': 6,
    'MIN_RR_RATIO': 0,

    # Stage 3: Price Action (DISABLED)
    'USE_PRICE_ACTION': False,  # DISABLED - only use ML + Grok AI
    'MIN_PRICE_ACTION_SCORE': 5,
    'SR_LOOKBACK_CANDLES': 50,
    'SR_PROXIMITY_PCT': 0.5,
    'VOLUME_CONFIRMATION_RATIO': 1.5,

    # Stage 4: HTF Alignment (DISABLED)
    'USE_HTF_ALIGNMENT': False,  # DISABLED - only use ML + Grok AI

    # Stage 5: AI Check (GROK)
    'USE_AI_CHECK': True,
    'AI_PROVIDER': 'grok',
    'AI_VALIDATOR_MODE': 'all',  # Check ALL signals
    'AI_CHECK_BORDERLINE_ONLY': False,
    'AI_MIN_SCORE_FOR_CHECK': 0,
    'AI_MAX_SCORE_FOR_CHECK': 15,

    # AI API Keys
    'XAI_API_KEY': Config.XAI_API_KEY,
    'ANTHROPIC_API_KEY': '',
    'OPENAI_API_KEY': '',
    'GOOGLE_API_KEY': '',

    # AI Model
    'AI_MODEL': Config.GROK_MODEL,
    'AI_TIMEOUT_SECONDS': 10,
    'AI_MAX_RETRIES': 2,
    'AI_MIN_CONFIDENCE': 0.6,
}

print("\nPipeline Config:")
print(f"  ML Ensemble: {pipeline_config['USE_ML_ENSEMBLE']}")
print(f"  Smart Entry: {pipeline_config['USE_SMART_ENTRY']}")
print(f"  Price Action: {pipeline_config['USE_PRICE_ACTION']}")
print(f"  HTF Alignment: {pipeline_config['USE_HTF_ALIGNMENT']}")
print(f"  AI Check: {pipeline_config['USE_AI_CHECK']}")
print(f"  AI Provider: {pipeline_config['AI_PROVIDER']}")
print(f"  AI Model: {pipeline_config['AI_MODEL']}")
print(f"  AI Validator Mode: {pipeline_config['AI_VALIDATOR_MODE']}")

# Initialize pipeline WITHOUT ML models (test with price action only)
print("\nInitializing Entry Pipeline...")
pipeline = EntryPipeline(
    config=pipeline_config,
    models=None,  # No ML models for this test
    smart_entry_v2=None
)

print("\nStages enabled:")
print(f"  ML: {pipeline.use_ml}")
print(f"  Smart Entry: {pipeline.use_smart_entry}")
print(f"  Price Action: {pipeline.use_price_action}")
print(f"  HTF: {pipeline.use_htf}")
print(f"  AI: {pipeline.use_ai}")

if pipeline.ai_stage:
    print(f"\nAI Stage initialized:")
    print(f"  Enabled: {pipeline.ai_stage.enabled}")
    print(f"  Provider: {pipeline.ai_stage.provider.value}")
    print(f"  Client available: {pipeline.ai_stage.client is not None}")
    if pipeline.ai_stage.client:
        print(f"  Client is_available: {pipeline.ai_stage.client.is_available()}")

# Create sample DataFrame with bullish setup
print("\n" + "=" * 60)
print("Creating sample BULLISH setup for BTCUSDT...")
print("=" * 60)

data = {
    'timestamp': pd.date_range(start='2024-01-01', periods=100, freq='1H'),
    'open': np.random.uniform(43000, 44000, 100),
    'high': np.random.uniform(43500, 44500, 100),
    'low': np.random.uniform(42500, 43500, 100),
    'close': np.linspace(43000, 44000, 100),  # Uptrend
    'volume': np.random.uniform(100, 200, 100),
}
df = pd.DataFrame(data)

# Add indicators (simulate)
df['rsi'] = 55  # Neutral RSI
df['sma_20'] = df['close'].rolling(20).mean()
df['sma_50'] = df['close'].rolling(50).mean()
df['ema21'] = df['close'].ewm(span=21).mean()
df['ema50'] = df['close'].ewm(span=50).mean()
df['atr'] = (df['high'] - df['low']).rolling(14).mean()
df['volume_sma'] = df['volume'].rolling(20).mean()

print(f"\nDataframe created:")
print(f"  Rows: {len(df)}")
print(f"  Latest close: {df['close'].iloc[-1]:.2f}")
print(f"  Trend: BULLISH (uptrend)")

# Test pipeline evaluation
print("\n" + "=" * 60)
print("EVALUATING ENTRY THROUGH PIPELINE...")
print("=" * 60)

symbol = "BTCUSDT"

try:
    decision = pipeline.evaluate(
        symbol=symbol,
        df=df,
        X_features=None,  # No ML features
        df_higher=None,
        df_4h=None
    )

    print(f"\nPIPELINE DECISION:")
    print(f"  Should Enter: {decision.should_enter}")
    print(f"  Direction: {decision.direction.value}")
    print(f"  Confidence: {decision.confidence:.2%}")
    print(f"  Reason: {decision.reason}")

    if decision.entry_price:
        print(f"  Entry Price: {decision.entry_price:.2f}")
    if decision.stop_loss:
        print(f"  Stop Loss: {decision.stop_loss:.2f}")
    if decision.take_profit:
        print(f"  Take Profit: {decision.take_profit:.2f}")

    print(f"\nStages Passed: {decision.stages_passed}")
    print(f"Stages Failed: {decision.stages_failed}")

    print(f"\nStage Results:")
    for stage in decision.stage_results:
        status = "PASS" if stage.passed else "FAIL"
        print(f"  [{status}] {stage.stage_name}: {stage.reason}")
        if stage.details:
            print(f"       Details: {stage.details}")

    print(f"\nProcessing time: {decision.processing_time_ms:.2f}ms")

    # Check if Grok AI was called
    ai_stages = [s for s in decision.stage_results if s.stage_name == 'ai_check']
    if ai_stages:
        print("\n" + "=" * 60)
        print("GROK AI WAS CALLED!")
        print("=" * 60)
        ai_stage = ai_stages[0]
        print(f"  AI Decision: {'APPROVED' if ai_stage.passed else 'REJECTED'}")
        print(f"  AI Reason: {ai_stage.reason}")
        if ai_stage.details:
            print(f"  AI Details: {ai_stage.details}")
    else:
        print("\n" + "=" * 60)
        print("WARNING: GROK AI WAS NOT CALLED!")
        print("=" * 60)

except Exception as e:
    print(f"\nERROR: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("TEST COMPLETE")
print("=" * 60)
