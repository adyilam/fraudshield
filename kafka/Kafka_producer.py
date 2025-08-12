import json, time, random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    linger_ms=10
)

def gen_txn():
    return {
        'amount': round(random.expovariate(1/200),2),
        'is_foreign': int(random.random() < 0.05),
        'is_high_risk_country': int(random.random() < 0.02),
        'num_recent_transactions': random.randint(0,12)
    }

if __name__ == '__main__':
    print('Starting Kafka producer... (CTRL+C to stop)')
    try:
        while True:
            tx = gen_txn()
            producer.send('fraud_topic', tx)
            producer.flush()
            print('Produced:', tx)
            time.sleep(1)
    except KeyboardInterrupt:
        print('Producer stopped')