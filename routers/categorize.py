from fastapi import APIRouter
from models.schemas import TransactionInput, CategoryResponse
from models.categorizer import predict_category

router = APIRouter(prefix="/categorize", tags=["Categorization"])

@router.post("", response_model=CategoryResponse)
def categorize_transaction(data: TransactionInput):
    """
    Takes a transaction title and returns the predicted category
    using a TF-IDF + Logistic Regression model.
    """
    category, confidence = predict_category(data.title)
    return CategoryResponse(category=category, confidence=confidence)
