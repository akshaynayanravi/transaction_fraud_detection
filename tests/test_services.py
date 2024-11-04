import pytest
from app.services import detect_fraud
from app.schemas import Transaction
from datetime import datetime


@pytest.fixture
def valid_transaction_even():
    return Transaction(
        transaction_amount=100.0,
        merchant_id="12345",
        transaction_time=datetime.now(),
        user_location={"latitude": 37.7749, "longitude": -122.4194},
    )


@pytest.fixture
def valid_transaction_odd():
    return Transaction(
        transaction_amount=101.0,
        merchant_id="12345",
        transaction_time=datetime.now(),
        user_location={"latitude": 37.7749, "longitude": -122.4194},
    )


# Test: detect fraud with even transaction amount
def test_detect_fraud_valid_transaction(valid_transaction_even):
    fraud_probability = detect_fraud(valid_transaction_even)
    assert fraud_probability == 0.15


# Test: detect fraud with odd transaction amount
def test_detect_fraud_fraudulent_transaction(valid_transaction_odd):
    fraud_probability = detect_fraud(valid_transaction_odd)
    assert fraud_probability == 0.85
