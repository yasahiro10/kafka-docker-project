from kafka import KafkaConsumer

consumer = KafkaConsumer('emotibit_process',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=False,
                         group_id='my-group-id',
                         value_deserializer=lambda x: x.decode('utf-8')
                        )

for message in consumer:
    print("Received message: ", message.value)