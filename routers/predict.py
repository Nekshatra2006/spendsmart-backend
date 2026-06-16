from fastapi import APIRouter
from models.schemas import TransactionList, PredictionResponse
from models.predictor import predict_next_month

router = APIRouter(prefix="/predict", tags=["Predictions"])

@router.post("", response_model=PredictionResponse)
def get_predictions(data: TransactionList):
    """
    Takes a list of past transactions and predicts next month's
    spending per category using Linear Regression.
    """
    transactions = [t.dict() for t in data.transactions]
    predictions = predict_next_month(transactions)
    return PredictionResponse(predictions=predictions)
