from pydantic import BaseModel
from typing import List, Optional

class TransactionInput(BaseModel):
    title: str

class TransactionData(BaseModel):
    title: str
    amount: float
    category: str
    date: str
    isExpense: bool

class TransactionList(BaseModel):
    transactions: List[TransactionData]

class CategoryResponse(BaseModel):
    category: str
    confidence: float

class PredictionResponse(BaseModel):
    predictions: dict

class InsightResponse(BaseModel):
    total_spent: float
    top_category: str
    avg_daily_spend: float
    highest_day: str
    savings_tip: str
    category_totals: dict
