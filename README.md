# Kafka Docker Project

A Python project for working with Apache Kafka using Docker Compose.

## Features
- Kafka cluster with Docker Compose
- Zookeeper for cluster coordination
- Kafka UI for easy management
- Python producer and consumer examples

## Prerequisites
- Docker and Docker Compose
- Python 3.7+
- pip

## Quick Start

1. **Start Kafka cluster:**
   ```bash
   docker-compose up -d

## 🧩 What is each component?

##  🧱 1. Kafka Broker = The Server

    It's a Kafka process (usually running on a Docker container or VM)

    It stores messages and handles requests

    It can manage many topics and partitions

📌 You usually have 1–5+ brokers in a real Kafka cluster.

## 🗂️ 2. Kafka Topic = The Category or Channel

    A logical name that groups messages

    Producers send messages into a topic

    Consumers subscribe to a topic to read messages

📌 Think of it like a "channel" in Pub/Sub systems

Examples:

sensor-data
emotibit-raw
emotibit-processed
user-activity-logs

## ✉️ 3. Kafka Producer = The Sender

    It's a Python, Java, Node.js app that pushes data into Kafka topics

```python
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('sensor-data', b'{"temp": 36.5, "heart_rate": 88}')
```
📌 Producers don’t need to know where consumers are — they just send data to topics.

## 📥 4. Kafka Consumer = The Receiver

    It's a script/app that listens to topics and processes messages

from kafka import KafkaConsumer
consumer = KafkaConsumer('sensor-data', bootstrap_servers='localhost:9092')
for message in consumer:
    print("Received:", message.value)

📌 Consumers can work in groups, share load, and process data in real time.
