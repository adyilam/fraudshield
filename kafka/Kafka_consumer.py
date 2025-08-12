import json, requests, os
from kafka import KafkaConsumer

API_URL = os.getenv('API_URL','http://localhost:8000/predict')

consumer = KafkaConsumer(
    'fraud_topic',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='fraud-shield-group'
)

print('Kafka consumer listening on topic fraud_topic...')
for msg in consumer:
    tx = msg.value
    print('Consumed:', tx)
    try:
        r = requests.post(API_URL, json=tx, timeout=5)
        if r.status_code == 200:
            print('Scored:', r.json())
        else:
            print('API error:', r.status_code, r.text)
    except Exception as e:
        print('Error calling API:', e)