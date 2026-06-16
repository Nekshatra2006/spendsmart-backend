import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
from typing import List, Dict

CATEGORIES = ['Food', 'Transport', 'Shopping', 'Bills', 'Health', 'Entertainment', 'Other']

def parse_transactions(transactions: list) -> pd.DataFrame:
    rows = []
    for t in transactions:
        if t['isExpense']:
            rows.append({
                'category': t['category'],
                'amount': t['amount'],
                'date': pd.to_datetime(t['date']),
            })
    if not rows:
        return pd.DataFrame(columns=['category', 'amount', 'date'])
    return pd.DataFrame(rows)

def predict_next_month(transactions: list) -> Dict[str, float]:
    df = parse_transactions(transactions)
    if df.empty:
        return {}

    df['month'] = df['date'].dt.to_period('M')
    predictions = {}

    for category in CATEGORIES:
        cat_df = df[df['category'] == category]
        if cat_df.empty:
            continue

        # Monthly totals
        monthly = cat_df.groupby('month')['amount'].sum().reset_index()
        monthly['month_num'] = range(len(monthly))

        if len(monthly) < 2:
            # Not enough data — use average as fallback
            predictions[category] = float(monthly['amount'].mean())
            continue

        # Linear regression on monthly totals
        X = monthly[['month_num']].values
        y = monthly['amount'].values

        model = LinearRegression()
        model.fit(X, y)

        next_month_num = len(monthly)
        predicted = model.predict([[next_month_num]])[0]

        # Never predict negative spending
        predictions[category] = max(float(predicted), 0.0)

    return {k: round(v, 2) for k, v in predictions.items()}
