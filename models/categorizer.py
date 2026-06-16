import os
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

MODEL_PATH = "models/categorizer.pkl"

# Training data: (transaction description, category)
TRAINING_DATA = [
    # Food
    ("swiggy order", "Food"), ("zomato delivery", "Food"), ("restaurant", "Food"),
    ("cafe coffee day", "Food"), ("mcdonalds", "Food"), ("kfc", "Food"),
    ("pizza hut", "Food"), ("dominos", "Food"), ("hotel lunch", "Food"),
    ("groceries", "Food"), ("supermarket", "Food"), ("vegetables", "Food"),
    ("milk", "Food"), ("bakery", "Food"), ("juice", "Food"), ("tea", "Food"),
    ("dinner", "Food"), ("lunch", "Food"), ("breakfast", "Food"), ("biryani", "Food"),
    ("blinkit", "Food"), ("zepto", "Food"), ("bigbasket", "Food"), ("fruits", "Food"),

    # Transport
    ("uber ride", "Transport"), ("ola cab", "Transport"), ("auto rickshaw", "Transport"),
    ("petrol", "Transport"), ("fuel", "Transport"), ("bus ticket", "Transport"),
    ("metro card", "Transport"), ("rapido", "Transport"), ("train ticket", "Transport"),
    ("flight ticket", "Transport"), ("parking", "Transport"), ("toll", "Transport"),
    ("vehicle service", "Transport"), ("car wash", "Transport"), ("taxi", "Transport"),

    # Shopping
    ("amazon order", "Shopping"), ("flipkart", "Shopping"), ("meesho", "Shopping"),
    ("myntra", "Shopping"), ("clothes", "Shopping"), ("shoes", "Shopping"),
    ("shirt", "Shopping"), ("jeans", "Shopping"), ("accessories", "Shopping"),
    ("ajio", "Shopping"), ("nykaa", "Shopping"), ("electronics", "Shopping"),
    ("mobile", "Shopping"), ("laptop", "Shopping"), ("watch", "Shopping"),

    # Bills
    ("electricity bill", "Bills"), ("water bill", "Bills"), ("rent", "Bills"),
    ("internet bill", "Bills"), ("wifi", "Bills"), ("jio recharge", "Bills"),
    ("airtel recharge", "Bills"), ("gas bill", "Bills"), ("insurance", "Bills"),
    ("emi", "Bills"), ("loan payment", "Bills"), ("maintenance", "Bills"),
    ("dth recharge", "Bills"), ("broadband", "Bills"), ("society charges", "Bills"),

    # Health
    ("medicine", "Health"), ("pharmacy", "Health"), ("doctor", "Health"),
    ("hospital", "Health"), ("clinic", "Health"), ("gym", "Health"),
    ("fitness", "Health"), ("yoga", "Health"), ("health checkup", "Health"),
    ("dental", "Health"), ("eye care", "Health"), ("blood test", "Health"),
    ("apollo pharmacy", "Health"), ("medplus", "Health"), ("consultation", "Health"),

    # Entertainment
    ("netflix", "Entertainment"), ("amazon prime", "Entertainment"),
    ("hotstar", "Entertainment"), ("spotify", "Entertainment"),
    ("movie ticket", "Entertainment"), ("pvr", "Entertainment"),
    ("inox", "Entertainment"), ("book", "Entertainment"), ("gaming", "Entertainment"),
    ("concert", "Entertainment"), ("event", "Entertainment"), ("bookmyshow", "Entertainment"),
    ("youtube premium", "Entertainment"), ("zerodha", "Entertainment"),

    # Other
    ("atm withdrawal", "Other"), ("transfer", "Other"), ("miscellaneous", "Other"),
    ("gift", "Other"), ("donation", "Other"), ("temple", "Other"),
    ("stationery", "Other"), ("printing", "Other"), ("courier", "Other"),
]

def train_categorizer():
    texts = [d[0] for d in TRAINING_DATA]
    labels = [d[1] for d in TRAINING_DATA]

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(ngram_range=(1, 2), lowercase=True)),
        ('clf', LogisticRegression(max_iter=1000, C=5.0)),
    ])
    pipeline.fit(texts, labels)

    os.makedirs("models", exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)
    print("✅ Categorizer model trained and saved.")
    return pipeline

def load_categorizer():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return train_categorizer()

def predict_category(title: str) -> tuple[str, float]:
    model = load_categorizer()
    proba = model.predict_proba([title.lower()])[0]
    classes = model.classes_
    top_idx = np.argmax(proba)
    return classes[top_idx], float(proba[top_idx])
