from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import categorize, predict, insights

app = FastAPI(
    title="SpendSmart API",
    description="ML-powered expense tracking backend",
    version="1.0.0"
)

# Allow Flutter app to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(categorize.router)
app.include_router(predict.router)
app.include_router(insights.router)

@app.get("/")
def root():
    return {"status": "SpendSmart API is running 🚀"}
