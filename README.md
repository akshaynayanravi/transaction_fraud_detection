# Transaction Fraud Detection API

```text
Question 2: ML Model API Wrapper

Design and implement an API wrapper for a dummy transaction fraud detection model.

Transaction Model
- transaction_amount: float (positive)
- merchant_id: string
- transaction_time: datetime
- user_location: dict with latitude and longitude

Dummy Model Logic
Use a simple rule-based model:
    IF transaction_amount odd number:
        return 0.85  # High probability of fraud
    ELSE:
        return 0.15  # Low probability of fraud
    
    Example:
    - Amount 100.00 → 0.15 (likely valid) - Amount 101.00 → 0.85 (likely fraud)

Requirements Implement endpoints:
1. POST /predict: Single transaction prediction
2. POST /predict/batch: Batch predictions (max 100)

Include:
● Input validation
● Error handling
● Response time monitoring
● Request volume tracking

Note
Use any web framework of your choice. Focus on API design and monitoring rather than the model logic.
```

## Project Structure
```plaintext
transaction_fraud_detection/
├── app/
│   ├── api.py                   # API layer with routing
|   ├── schemas.py               # Pydantic models and schemas for serializing and deserializing data
│   ├── services.py              # Business logic and fraud detection services
├── core/                        # Core configurations and security
├── tests/                       # Unit and integration tests
├── main.py                      # Entry point for FastAPI application
└── README.md                    # Project documentation
```

## Instructions

### Prerequisites
- `Python 3.8+`
- `Poetry`

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/akshaynayanravi/transaction_fraud_detection.git
    cd transaction_fraud_detection
    ```

2. Setting up virtual environment using Poetry:
    ```bash
    poetry install
    poetry shell
    ```

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

4. Run unit tests:
   ```bash
   pytest .
   ```
   
5. Generate coverage report:
   ```bash
   coverage run -m pytest . -v && coverage report -m
   ```
    Note: Current coverage stands at 96%

## API Endpoints

### For Documentation:
- http://127.0.0.1:8000/docs

### 1. Predict Fraud for a Single Transaction
- Endpoint: POST /api/fraud/predict
- Description: Returns the probability of fraud for a single transaction.
- Request Body:
  ```bash
  {
    "transaction_amount": 100.0,
    "merchant_id": "12345",
    "transaction_time": "2023-09-15T10:00:00",
    "user_location": {
      "latitude": 37.7749,
      "longitude": -122.4194
    }
  }
  ```
- Response:
  ```bash
  {
    "fraud_probability": 0.15
  }
  ```
  
### 2. Batch Fraud Prediction
- Endpoint: POST /api/fraud/predict/batch
- Description: Returns fraud probabilities for a batch of up to 100 transactions.
- Request Body:
  ```bash
  [
    {
      "transaction_amount": 100.0,
      "merchant_id": "12345",
      "transaction_time": "2023-09-15T10:00:00",
      "user_location": {
        "latitude": 37.7749,
        "longitude": -122.4194
      }
    },
    {
      "transaction_amount": 101.0,
      "merchant_id": "12346",
      "transaction_time": "2023-09-15T11:00:00",
      "user_location": {
        "latitude": 40.7128,
        "longitude": -74.0060
      }
    }
  ]
  ```

- Response:
  ```bash
  {
    "predictions": [
      {"fraud_probability": 0.15},
      {"fraud_probability": 0.85}
    ]
  }
  ```

## Project Improvements
### Future improvements for this project may include:
- Machine Learning Model: Implement an ML-based fraud detection model.
- Database Integration: Add support for storing transactions and fraud predictions.
- User Authentication: Secure the endpoints with JWT or OAuth2 authentication.
- Enhanced Batch Processing: Allow for asynchronous batch processing for larger datasets.
