from fastapi import APIRouter
from models.schemas import TransactionList, InsightResponse
import pandas as pd
from collections import defaultdict

router = APIRouter(prefix="/insights", tags=["Insights"])

SAVINGS_TIPS = {
    "Food": "Try meal prepping at home — it can cut food expenses by up to 40%.",
    "Transport": "Consider carpooling or using public transport more often.",
    "Shopping": "Use a 24-hour rule before making non-essential purchases.",
    "Bills": "Review your subscriptions — cancel ones you rarely use.",
    "Health": "Invest in preventive checkups to avoid bigger costs later.",
    "Entertainment": "Look for free local events and use family streaming plans.",
    "Other": "Track every small expense — they add up faster than you think.",
}

@router.post("", response_model=InsightResponse)
def get_insights(data: TransactionList):
    """
    Returns spending insights: totals by category, top spending day,
    average daily spend, and a personalized savings tip.
    """
    transactions = [t.dict() for t in data.transactions]
    expenses = [t for t in transactions if t['isExpense']]

    if not expenses:
        return InsightResponse(
            total_spent=0,
            top_category="N/A",
            avg_daily_spend=0,
            highest_day="N/A",
            savings_tip="Start adding transactions to get insights!",
            category_totals={},
        )

    df = pd.DataFrame(expenses)
    df['date'] = pd.to_datetime(df['date'])
    df['day'] = df['date'].dt.strftime('%A')

    # Category totals
    category_totals = df.groupby('category')['amount'].sum().to_dict()
    category_totals = {k: round(v, 2) for k, v in category_totals.items()}

    # Top category
    top_category = max(category_totals, key=category_totals.get)

    # Total spent
    total_spent = round(sum(category_totals.values()), 2)

    # Avg daily spend
    num_days = max((df['date'].max() - df['date'].min()).days, 1)
    avg_daily = round(total_spent / num_days, 2)

    # Highest spending day of week
    day_totals = df.groupby('day')['amount'].sum()
    highest_day = day_totals.idxmax()

    # Savings tip based on top category
    tip = SAVINGS_TIPS.get(top_category, SAVINGS_TIPS["Other"])

    return InsightResponse(
        total_spent=total_spent,
        top_category=top_category,
        avg_daily_spend=avg_daily,
        highest_day=highest_day,
        savings_tip=tip,
        category_totals=category_totals,
    )
