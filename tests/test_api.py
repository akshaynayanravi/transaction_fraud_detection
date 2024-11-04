import pytest
from fastapi.testclient import TestClient
from main import app
from datetime import datetime

client = TestClient(app)

# Test data for fraud detection
transaction_data_even = {
    "transaction_amount": 100.0,
    "merchant_id": "12345",
    "transaction_time": datetime.now().isoformat(),
    "user_location": {"latitude": 37.7749, "longitude": -122.4194},
}

transaction_data_odd = {
    "transaction_amount": 101.0,
    "merchant_id": "12345",
    "transaction_time": datetime.now().isoformat(),
    "user_location": {"latitude": 37.7749, "longitude": -122.4194},
}


# Test: Predict with even transaction amount
def test_predict_valid_transaction():
    response = client.post("/api/fraud/predict", json=transaction_data_even)
    assert response.status_code == 200
    assert response.json() == {"fraud_probability": 0.15}


# Test: Predict with odd transaction amount
def test_predict_fraudulent_transaction():
    response = client.post("/api/fraud/predict", json=transaction_data_odd)
    assert response.status_code == 200
    assert response.json() == {"fraud_probability": 0.85}


# Test: Predict with invalid transaction amount (negative)
def test_predict_invalid_transaction_amount():
    invalid_data = transaction_data_even.copy()
    invalid_data["transaction_amount"] = -100.0  # Invalid amount
    response = client.post("/api/fraud/predict", json=invalid_data)
    assert response.status_code == 422  # Unprocessable Entity for validation error


def test_batch_predict_valid_transactions():
    transactions = [transaction_data_even, transaction_data_odd]
    response = client.post("/api/fraud/predict/batch", json=transactions)
    assert response.status_code == 200
    assert response.json() == {
        "predictions": [{"fraud_probability": 0.15}, {"fraud_probability": 0.85}]
    }


# Test: Batch predict with more than 100 transactions
def test_batch_predict_too_many_transactions():
    transactions = [transaction_data_even] * 101  # 101 transactions, exceeding limit
    response = client.post("/api/fraud/predict/batch", json=transactions)
    assert response.status_code == 422  # Exceeds limit, should raise validation error
