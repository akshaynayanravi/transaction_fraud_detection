from app.schemas import Transaction


def detect_fraud(transaction: Transaction) -> float:
    """Simple rule-based fraud detection logic."""
    return 0.85 if int(transaction.transaction_amount) % 2 != 0 else 0.15
