from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


class Location(BaseModel):
    latitude: float
    longitude: float


class Transaction(BaseModel):
    transaction_amount: float = Field(
        gt=0, description="Transaction amount must be positive"
    )
    merchant_id: str
    transaction_time: datetime
    user_location: Location


class PredictionResponse(BaseModel):
    fraud_probability: float


class BatchPredictionResponse(BaseModel):
    predictions: List[PredictionResponse]
