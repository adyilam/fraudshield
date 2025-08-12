# FraudShield

Real-time fraud detection pipeline using Kafka, FastAPI, and machine learning

Real-time fraud detection pipeline (local).

## Structure
- api/Fraud_api.py — FastAPI app
- model/Train_model.py — trains and saves models/Fraud_model.pkl
- data/sample_transactions.csv — sample data
- kafka/Kafka_producer.py — producer script
- kafka/Kafka_consumer.py — consumer script that calls API
- kafka/bin/kafka-server-start.sh — helper script (placeholder)
- kafka/config/server.properties — KRaft-mode config (local testing)
- models/Fraud_model.pkl — trained model artifact (created by Train_model.py)
- requirements.txt — python dependencies
- docker-compose.yml — optional Docker Compose for Kafka & Zookeeper
- venu/ — placeholder for virtual environment or notes

## Quickstart (local, without Docker)

1. Create & activate venv:
```bash
python3 -m venv venu
source venu/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Train model:
```bash
python model/Train_model.py
```

4. Start FastAPI:
```bash
uvicorn api.Fraud_api:app --reload
```

5. Run Kafka (use Docker or local Kafka). If Kafka runs at localhost:9092, then:
```bash
python kafka/Kafka_producer.py    # in separate terminal to produce messages
python kafka/Kafka_consumer.py   # in another terminal to consume & score
```

## Notes
- This is a local dev/demo setup. The model is synthetic for demonstration purposes.
- For production, replace with real training data, secure Kafka, and add monitoring.
