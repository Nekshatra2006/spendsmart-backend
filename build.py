#!/usr/bin/env python3
"""
Run this as the build step on Render to pre-train the ML model.
Build command: python build.py && echo 'Build done'
Start command: uvicorn main:app --host 0.0.0.0 --port $PORT
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from models.categorizer import train_categorizer

print("🤖 Training categorizer model...")
train_categorizer()
print("✅ Model ready.")
