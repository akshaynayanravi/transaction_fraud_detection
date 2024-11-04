# Transaction Fraud Detection API

## Overview
The Transaction Fraud Detection API is a FastAPI-based project designed to detect potential fraudulent transactions using a rule-based approach. This project provides RESTful endpoints for single and batch transaction predictions, applying a simple fraud detection model that flags transactions based on the amount.

### Features
- **Single Transaction Prediction**: Predict the likelihood of fraud for a single transaction.
- **Batch Transaction Prediction**: Predict fraud likelihood for a batch of transactions (up to 100).
- **API Versioning**: Modular and scalable project structure with versioned endpoints.
- **Error Handling & Input Validation**: Validates input data for better reliability.
- **Modular Structure**: Organized for easy maintenance and scalability.

---

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

## Getting Started

### Requirements
- `Python 3.8+`
- `FastAPI`
- `Uvicorn (for local development)`
- `pytest (for testing)`

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/akshaynayanravi/transaction_fraud_detection.git
    cd transaction_fraud_detection
    ```

2. Install Poetry:

    ```bash
    poetry install
    poetry shell
    ```

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

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

## Testing

### Run Tests:
- To run unit and integration tests, use the following command:
  ```bash
  pytest tests/
  ```

### Testing Components:
- API Tests: Located in tests/test_api, contains tests for the fraud prediction endpoints.
- Service Tests: Located in tests/test_services, contains tests for the fraud detection logic.

## Project Improvements
### Future improvements for this project may include:
- Machine Learning Model: Implement an ML-based fraud detection model.
- Database Integration: Add support for storing transactions and fraud predictions.
- User Authentication: Secure the endpoints with JWT or OAuth2 authentication.
- Enhanced Batch Processing: Allow for asynchronous batch processing for larger datasets.
