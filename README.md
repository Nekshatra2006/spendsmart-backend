# 💰 SpendSmart — AI-Powered Expense Tracker

> A full-stack mobile application that tracks expenses, auto-categorizes transactions using Machine Learning, and predicts future spending patterns.

---

## 📱 Screenshots

> Add screenshots of your app here after running it!

---

## 🚀 Features

- 🔐 **Firebase Authentication** — Secure email/password login & signup
- 🤖 **AI Auto-Categorization** — ML model automatically categorizes transactions (Food, Transport, Bills, etc.)
- 📊 **Spending Insights** — Visual breakdown of spending by category with pie charts
- 🔮 **Future Predictions** — Linear Regression model predicts next month's spending per category
- 💰 **Budget Tracker** — Set monthly budgets per category with real-time alerts
- ☁️ **Cloud Sync** — All data stored in Firebase Firestore, synced in real-time
- 🌙 **Dark Mode UI** — Beautiful dark-themed Flutter UI

---

## 🛠️ Tech Stack

### Frontend (Mobile)
| Technology | Purpose |
|---|---|
| Flutter (Dart) | Cross-platform mobile app |
| Firebase Auth | User authentication |
| Cloud Firestore | Real-time database |
| fl_chart | Spending charts |
| HTTP | API calls to backend |

### Backend (ML API)
| Technology | Purpose |
|---|---|
| Python | Core language |
| FastAPI | REST API framework |
| Scikit-learn | ML models (TF-IDF + Logistic Regression, Linear Regression) |
| Pandas / NumPy | Data processing |
| Render | Cloud deployment |

---

## 🧠 ML Models

### 1. Transaction Categorizer
- **Algorithm:** TF-IDF Vectorizer + Logistic Regression Pipeline
- **Input:** Transaction description text
- **Output:** Category (Food, Transport, Shopping, Bills, Health, Entertainment, Other)
- **Training Data:** 100+ labeled Indian transaction descriptions
- **Accuracy:** ~85%

### 2. Spending Predictor
- **Algorithm:** Linear Regression per category
- **Input:** Past transaction history
- **Output:** Predicted spending for next month per category
- **Approach:** Monthly aggregation → trend extrapolation

---

## 📁 Project Structure

```
SpendSmart/
├── frontend/                    # Flutter Mobile App
│   └── lib/
│       ├── main.dart            # App entry point
│       ├── screens/             # UI screens
│       │   ├── home_screen.dart
│       │   ├── add_transaction_screen.dart
│       │   ├── insights_screen.dart
│       │   ├── budget_screen.dart
│       │   └── auth/
│       │       ├── login_screen.dart
│       │       └── signup_screen.dart
│       ├── services/            # Business logic
│       │   ├── api_service.dart
│       │   ├── auth_service.dart
│       │   └── firestore_service.dart
│       ├── models/              # Data models
│       │   └── transaction_model.dart
│       ├── widgets/             # Reusable UI components
│       │   ├── transaction_card.dart
│       │   └── spending_chart.dart
│       └── theme/               # Dark theme config
│           └── app_theme.dart
│
└── backend/                     # Python FastAPI + ML
    ├── main.py                  # FastAPI app
    ├── build.py                 # Model training script
    ├── requirements.txt
    ├── models/
    │   ├── categorizer.py       # TF-IDF + LogReg model
    │   ├── predictor.py         # Linear Regression model
    │   └── schemas.py           # Pydantic schemas
    └── routers/
        ├── categorize.py        # POST /categorize
        ├── predict.py           # POST /predict
        └── insights.py          # POST /insights
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/categorize` | Auto-categorize a transaction |
| POST | `/predict` | Predict next month's spending |
| POST | `/insights` | Get spending insights & tips |

### Example

```bash
# Categorize a transaction
curl -X POST https://spendsmart-backend-ohen.onrender.com/categorize \
  -H "Content-Type: application/json" \
  -d '{"title": "swiggy order"}'

# Response
{"category": "Food", "confidence": 0.87}
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Flutter SDK
- Python 3.10+
- Firebase account

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python build.py        # Train ML models
uvicorn main:app --reload
```

### Frontend Setup
```bash
cd frontend
flutter pub get
# Add google-services.json to android/app/
flutter run
```

---

## 🌐 Live Demo

- **Backend API:** https://spendsmart-backend-ohen.onrender.com
- **API Docs:** https://spendsmart-backend-ohen.onrender.com/docs

---

## 👨‍💻 Author

**Nekshatra**
- GitHub: [@Nekshatra2006](https://github.com/Nekshatra2006)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
