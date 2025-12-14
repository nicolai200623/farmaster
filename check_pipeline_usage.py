#!/usr/bin/env python3
"""
Check if Entry Pipeline is actually being used in signal generation
"""
import sys
import os

# Read signal_generator.py
print("=" * 60)
print("CHECKING ENTRY PIPELINE USAGE IN CODE")
print("=" * 60)

with open('trading/signal_generator.py', 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.split('\n')

print("\n1. Checking if Entry Pipeline initialization exists:")
print("-" * 60)
init_found = False
for i, line in enumerate(lines):
    if 'self.entry_pipeline = None' in line:
        print(f"Line {i+1}: {line.strip()}")
        init_found = True
        # Show next 10 lines
        for j in range(i+1, min(i+11, len(lines))):
            print(f"Line {j+1}: {lines[j].strip()}")
        break

if not init_found:
    print("❌ Entry Pipeline initialization NOT FOUND!")

print("\n2. Checking if Entry Pipeline is used in generate_signal:")
print("-" * 60)
usage_found = False
for i, line in enumerate(lines):
    if 'if self.entry_pipeline is not None:' in line:
        print(f"✅ Found at line {i+1}: {line.strip()}")
        usage_found = True
        # Show context
        for j in range(max(0, i-2), min(i+8, len(lines))):
            marker = ">>>" if j == i else "   "
            print(f"{marker} Line {j+1}: {lines[j].strip()}")
        break

if not usage_found:
    print("❌ Entry Pipeline usage NOT FOUND in generate_signal!")
    print("\nSearching for alternative patterns...")
    # Check if SmartEntryV2 is being used instead
    for i, line in enumerate(lines):
        if 'if Config.USE_SMART_ENTRY_V2' in line:
            print(f"\n⚠️ Found SmartEntryV2 check at line {i+1}")
            for j in range(i, min(i+5, len(lines))):
                print(f"Line {j+1}: {lines[j].strip()}")

print("\n3. Checking _generate_signal_with_pipeline method:")
print("-" * 60)
method_found = False
for i, line in enumerate(lines):
    if 'def _generate_signal_with_pipeline' in line:
        print(f"✅ Found at line {i+1}: {line.strip()}")
        method_found = True
        break

if not method_found:
    print("❌ _generate_signal_with_pipeline method NOT FOUND!")

print("\n4. Checking Config.USE_ENTRY_PIPELINE:")
print("-" * 60)

from config import Config
print(f"Config.USE_ENTRY_PIPELINE: {Config.USE_ENTRY_PIPELINE}")
print(f"Config.USE_SMART_ENTRY_V2: {Config.USE_SMART_ENTRY_V2}")
print(f"Config.USE_AI_CHECK: {Config.USE_AI_CHECK}")

print("\n" + "=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60)

# Recommendation
if usage_found and method_found and Config.USE_ENTRY_PIPELINE:
    print("\n✅ Entry Pipeline SHOULD be working!")
    print("   If not being used, check:")
    print("   1. Bot instance is using latest code")
    print("   2. No errors during pipeline initialization")
    print("   3. self.entry_pipeline is not None at runtime")
else:
    print("\n❌ Entry Pipeline will NOT work!")
    if not usage_found:
        print("   - Pipeline check not found in generate_signal")
    if not method_found:
        print("   - _generate_signal_with_pipeline method missing")
    if not Config.USE_ENTRY_PIPELINE:
        print("   - Config.USE_ENTRY_PIPELINE is False")
