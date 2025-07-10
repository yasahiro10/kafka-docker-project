from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer = lambda x: json.dumps(x).encode("utf-8")
)
for i in range(100):
    message = {'id':i,'message':f'hello from kafka{i}'}
    producer.send("emotibit_process",value=message)
    print(f'sent:{message}')
    time.sleep(1)

producer.flush()
producer.close()