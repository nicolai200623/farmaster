#!/usr/bin/env python3
"""
🧪 Test scaler loading - Debug script
Kiểm tra xem scaler có load được không
"""

import os
import pickle
import sys

print("=" * 60)
print("🧪 TESTING SCALER LOADING")
print("=" * 60)

# Check sklearn version
try:
    import sklearn
    print(f"\n✅ sklearn version: {sklearn.__version__}")
except ImportError:
    print("❌ sklearn not installed!")
    sys.exit(1)

# Check scaler file exists
scaler_path = 'models/scaler.pkl'
print(f"\n📁 Checking scaler file: {scaler_path}")

if not os.path.exists(scaler_path):
    print(f"❌ File not found: {scaler_path}")
    print("   Please make sure scaler.pkl is in the models/ directory")
    sys.exit(1)

# Get file size
file_size = os.path.getsize(scaler_path)
print(f"   File size: {file_size} bytes")

if file_size < 100:
    print("⚠️ WARNING: File seems too small, might be corrupted!")

# Try to load scaler
print(f"\n🔄 Loading scaler...")
try:
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)
    print(f"✅ Scaler loaded successfully!")
    print(f"   Type: {type(scaler)}")
    print(f"   Class: {scaler.__class__.__name__}")
except Exception as e:
    print(f"❌ Failed to load scaler: {e}")
    print(f"\n💡 This usually means sklearn version mismatch!")
    print(f"   Local sklearn might be different from VPS sklearn")
    sys.exit(1)

# Check if scaler is fitted
print(f"\n🔍 Checking if scaler is fitted...")
try:
    # Check for fitted attributes
    if hasattr(scaler, 'data_min_'):
        print(f"✅ Scaler is FITTED!")
        print(f"   Feature range: {scaler.feature_range}")
        print(f"   n_features: {scaler.n_features_in_}")
        print(f"   data_min: {scaler.data_min_[:5]}... (first 5)")
        print(f"   data_max: {scaler.data_max_[:5]}... (first 5)")
    else:
        print(f"❌ Scaler is NOT fitted!")
        print(f"   This means the scaler.pkl was saved BEFORE fitting")
        print(f"   The training script has a bug!")
except Exception as e:
    print(f"❌ Error checking scaler: {e}")
    sys.exit(1)

# Test transform
print(f"\n🧪 Testing transform...")
try:
    import numpy as np
    # Create dummy data with correct shape (23 features)
    dummy_data = np.random.rand(1, scaler.n_features_in_)
    result = scaler.transform(dummy_data)
    print(f"✅ Transform works!")
    print(f"   Input shape: {dummy_data.shape}")
    print(f"   Output shape: {result.shape}")
except Exception as e:
    print(f"❌ Transform failed: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✅ ALL TESTS PASSED!")
print("=" * 60)
print("\n💡 If this works on LOCAL but fails on VPS:")
print("   1. Check sklearn versions match:")
print("      LOCAL:  pip show scikit-learn")
print("      VPS:    pip3 show scikit-learn")
print("   2. If versions differ, regenerate scaler on VPS:")
print("      python3 scripts/auto_retrain.py --days 15")
print("   3. Or upgrade sklearn on both to same version")

