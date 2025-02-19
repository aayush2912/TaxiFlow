# 🛠️ TaxiFlow: Real-Time Stream Processing with Kafka

## 📅 Step 6: Stream Processing

This phase focuses on **real-time data ingestion, processing, and analytics** using **Apache Kafka and Kafka Streams**. The goal is to enable **low-latency data streaming, live data transformation, and event-driven architecture** for NYC Taxi trip data.

---

## 🔧 Key Components

### **1️⃣ Kafka Infrastructure Setup**
- **Zookeeper & Kafka Brokers** for cluster management.
- **Kafka Topics** for data ingestion.
- **Schema Registry** for structured messages.

### **2️⃣ Stream Processing Architecture**
- **Kafka Producers** to ingest live taxi data.
- **Kafka Streams** to process and transform data in real-time.
- **Kafka Consumers** to store processed data in BigQuery.

### **3️⃣ Real-Time Analytics & Monitoring**
- **ksqlDB for stream analytics**.
- **Prometheus & Grafana** for monitoring.
- **Alerting & Logging Mechanisms** for failure handling.

---

## 🚀 Kafka Infrastructure Setup

### **1️⃣ Start Kafka & Zookeeper**
Ensure Kafka is running locally or in a cloud environment:
```bash
docker-compose up -d
```

### **2️⃣ Create Kafka Topics**
Define topics for taxi trip data ingestion:
```bash
kafka-topics.sh --create --topic taxi-trips --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```

### **3️⃣ Check Existing Topics**
List available Kafka topics:
```bash
kafka-topics.sh --list --bootstrap-server localhost:9092
```

---

## 🔧 Stream Processing with Kafka Streams

### **1️⃣ Writing a Kafka Producer for Taxi Data**
Example Python producer (`producer.py`):
```python
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

data = {"trip_id": "1234", "pickup_time": "2025-02-18T10:00:00", "fare": 15.75}
while True:
    producer.send("taxi-trips", data)
    time.sleep(5)
```

### **2️⃣ Kafka Streams Application for Processing**
Example Kafka Streams app (`streams.py`):
```python
from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer("taxi-trips", bootstrap_servers='localhost:9092', value_deserializer=lambda v: json.loads(v.decode('utf-8')))
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for message in consumer:
    data = message.value
    data["surge_price"] = data["fare"] * 1.2  # Apply surge pricing logic
    producer.send("processed-taxi-trips", data)
```

### **3️⃣ Consuming Processed Data**
Example consumer (`consumer.py`):
```python
consumer = KafkaConsumer("processed-taxi-trips", bootstrap_servers='localhost:9092', value_deserializer=lambda v: json.loads(v.decode('utf-8')))

for message in consumer:
    print("Processed Data:", message.value)
```

---

## 📊 Real-Time Analytics with ksqlDB

### **1️⃣ KSQL DB Testing Commands**
We used `commands.md` to test our project with the following ksqlDB queries:

- **Create Streams:**
```sql
CREATE STREAM ride_streams (
    VendorId varchar, 
    trip_distance double,
    payment_type varchar
)  WITH (KAFKA_TOPIC='rides',
        VALUE_FORMAT='JSON');
```

- **Query Stream:**
```sql
SELECT * FROM RIDE_STREAMS 
EMIT CHANGES;
```

- **Query Stream Count:**
```sql
SELECT VENDORID, count(*) FROM RIDE_STREAMS 
GROUP BY VENDORID
EMIT CHANGES;
```

- **Query with Filters:**
```sql
SELECT payment_type, count(*) FROM RIDE_STREAMS 
WHERE payment_type IN ('1', '2')
GROUP BY payment_type
EMIT CHANGES;
```

- **Query with Window Functions:**
```sql
CREATE TABLE payment_type_sessions AS
  SELECT payment_type,
         count(*)
  FROM  RIDE_STREAMS 
  WINDOW SESSION (60 SECONDS)
  GROUP BY payment_type
  EMIT CHANGES;
```

For more details, refer to the [KSQL DB Documentation](https://docs.ksqldb.io/en/latest/developer-guide/ksqldb-reference/quick-reference/).

---

## ☁️ Streaming Data to BigQuery

### **1️⃣ Kafka Connect Configuration**
Use **Kafka Connect** to stream processed data to **BigQuery**:
```json
{
  "name": "bigquery-sink",
  "config": {
    "connector.class": "com.wepay.kafka.connect.bigquery.BigQuerySinkConnector",
    "topics": "processed-taxi-trips",
    "project.id": "taxi-rides-ny",
    "dataset.id": "analytics",
    "table.id": "realtime_taxi_trips",
    "autoCreateTables": "true"
  }
}
```

### **2️⃣ Deploy Kafka Connect Sink**
```bash
curl -X POST -H "Content-Type: application/json" --data @bigquery_sink.json http://localhost:8083/connectors
```

---

## 📊 Monitoring & Alerting

### **1️⃣ Prometheus Metrics Exporter**
Monitor Kafka cluster performance using Prometheus:
```bash
docker-compose up -d prometheus grafana
```

### **2️⃣ Configure Alerts in Grafana**
- Create custom dashboards to track message latency.
- Set alerts for **high message lag** and **consumer failures**.

By implementing **real-time stream processing with Kafka, ksqlDB, and BigQuery**, this phase ensures **low-latency, event-driven analytics for NYC Taxi data**. 🚀 This completes the TaxiFlow Data Pipeline! 🎉

