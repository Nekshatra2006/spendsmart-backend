#!/bin/bash
echo "🚀 Starting SpendSmart Backend..."

# Install dependencies
pip install -r requirements.txt

# Train the categorizer model on first run
python3 -c "from models.categorizer import train_categorizer; train_categorizer()"

# Start FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
