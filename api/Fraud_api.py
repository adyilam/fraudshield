from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib, os, numpy as np, pandas as pd

app = FastAPI(title='FraudShield API')

MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models', 'Fraud_model.pkl'))

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None

class Transaction(BaseModel):
    amount: float
    is_foreign: int = 0
    is_high_risk_country: int = 0
    num_recent_transactions: int = 0

@app.get('/health')
def health():
    return {'status': 'ok', 'model_loaded': model is not None}

@app.post('/predict')
def predict(tx: Transaction):
    if model is None:
        raise HTTPException(status_code=500, detail='Model not loaded. Run model/Train_model.py first.')
    try:
        arr = np.array([[tx.amount, tx.is_foreign, tx.is_high_risk_country, tx.num_recent_transactions]])
        pred = model.predict(arr)[0]
        prob = float(model.predict_proba(arr)[0][1]) if hasattr(model, 'predict_proba') else None
        return {'is_fraud': bool(int(pred)), 'fraud_probability': prob}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))