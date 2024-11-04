from fastapi import APIRouter, HTTPException
from pydantic import conlist

from app.schemas import Transaction, PredictionResponse, BatchPredictionResponse
from app.services import detect_fraud

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
async def predict_fraud(transaction: Transaction):
    try:
        fraud_probability = detect_fraud(transaction)
        return PredictionResponse(fraud_probability=fraud_probability)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/predict/batch", response_model=BatchPredictionResponse)
async def predict_batch(transactions: conlist(Transaction, max_length=100)):
    try:
        # Run dummy model for each transaction
        predictions = [
            PredictionResponse(fraud_probability=detect_fraud(tx))
            for tx in transactions
        ]
        return BatchPredictionResponse(predictions=predictions)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
