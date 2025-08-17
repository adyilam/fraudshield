# FraudShield

FraudShield is a modular, real-time fraud detection system designed for high-throughput environments.
It uses Apache Kafka for streaming, FastAPI for API services, and machine learning models for intelligent fraud detection.

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
6. Sample Swagger test
   <img width="1399" height="654" alt="Screenshot 2025-08-16 at 9 45 34 PM" src="https://github.com/user-attachments/assets/3dc22629-e784-4a3b-903f-679f0527893e" />

   <img width="1166" height="620" alt="Screenshot 2025-08-16 at 9 46 31 PM" src="https://github.com/user-attachments/assets/c4e653e4-51fd-4d18-b78c-8bef2fd788a9" />

      <img width="728" height="654" alt="Screenshot 2025-08-16 at 9 49 21 PM" src="https://github.com/user-attachments/assets/622ec7f4-eff1-4edf-b1f2-96acfa7e7bdf" />

     <img width="736" height="702" alt="Screenshot 2025-08-16 at 9 55 41 PM" src="https://github.com/user-attachments/assets/6ed78b46-b7de-4e00-a8f8-acb93fb8bd7e" />





## Notes
- This is a local dev/demo setup. The model is synthetic for demonstration purposes.
- For production, replace with real training data, secure Kafka, and add monitoring.
