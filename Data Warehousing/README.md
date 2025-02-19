# 🛠️ TaxiFlow: Data Warehousing with PostgreSQL & BigQuery

## 📅 Step 3: Data Warehousing

This phase focuses on **storing, structuring, and optimizing taxi data** in both **PostgreSQL (local development)** and **Google BigQuery (cloud environment)**. The goal is to ensure efficient querying, scalability, and structured storage for analytics.

---

## 🔧 Key Components

### **1️⃣ Local Development with PostgreSQL**
- **PostgreSQL setup** in Docker for local testing and transformations.
- **Schema design** optimized for taxi trip data.
- **Indexing & partitioning** for query performance.

### **2️⃣ Cloud Implementation with BigQuery**
- **Dataset organization** following best practices.
- **Partitioning & clustering** to optimize performance.
- **Access control** to manage security and data governance.

### **3️⃣ Data Loading & Transformation**
- **Batch loading** via Kestra pipelines.
- **Schema validation & integrity checks**.
- **Optimized query execution** with indexing and table design.

### **4️⃣ Machine Learning with BigQuery ML**
- **Feature selection & model training** using `big_query_ml.sql`.
- **Tip prediction model** using **Linear Regression**.
- **Hyperparameter tuning** for model optimization.

---

## 🚀 PostgreSQL Implementation

### **1️⃣ Setup PostgreSQL via Docker**
Ensure PostgreSQL is installed and running:
```bash
docker-compose up -d postgres
```

Verify connection using:
```bash
psql -h localhost -U admin -d nyc_taxi_data
```

### **2️⃣ Schema Design**
Create table schema optimized for taxi trip data:
```sql
CREATE TABLE taxi_trips (
    trip_id SERIAL PRIMARY KEY,
    vendor_id INTEGER,
    pickup_datetime TIMESTAMP,
    dropoff_datetime TIMESTAMP,
    passenger_count INTEGER,
    trip_distance FLOAT,
    fare_amount FLOAT,
    total_amount FLOAT,
    payment_type INTEGER
);
```

### **3️⃣ Data Loading in PostgreSQL**
Load CSV data into PostgreSQL:
```bash
COPY taxi_trips FROM '/data/yellow_tripdata.csv' DELIMITER ',' CSV HEADER;
```

---

## ☁️ BigQuery Implementation

### **1️⃣ Setting Up BigQuery Dataset**
Create a dataset in BigQuery:
```sql
CREATE SCHEMA nyc_taxi_data OPTIONS(location='US');
```

### **2️⃣ Creating Optimized Tables**
Use partitioning & clustering to optimize queries:
```sql
CREATE TABLE nyc_taxi_data.taxi_trips (
    trip_id STRING,
    pickup_datetime TIMESTAMP,
    dropoff_datetime TIMESTAMP,
    passenger_count INT64,
    trip_distance FLOAT64,
    fare_amount FLOAT64,
    total_amount FLOAT64,
    payment_type INT64
)
PARTITION BY DATE(pickup_datetime)
CLUSTER BY vendor_id;
```

### **3️⃣ Loading Data into BigQuery**
Load data from Google Cloud Storage (GCS):
```bash
bq load --source_format=CSV --autodetect nyc_taxi_data.taxi_trips gs://nyc-taxi-data/raw/yellow_tripdata.csv
```

---

## 🎯 BigQuery ML Implementation

### **1️⃣ Feature Selection & Model Creation**
The `big_query_ml.sql` script selects key features for training and creates a structured ML-ready dataset:
```sql
SELECT passenger_count, trip_distance, PULocationID, DOLocationID, payment_type, fare_amount, tolls_amount, tip_amount
FROM `taxi-rides-ny.nytaxi.yellow_tripdata_partitioned` WHERE fare_amount != 0;
```

### **2️⃣ Creating ML Table**
Converting raw data into a structured ML table:
```sql
CREATE OR REPLACE TABLE `taxi-rides-ny.nytaxi.yellow_tripdata_ml` AS (
SELECT passenger_count, trip_distance, CAST(PULocationID AS STRING), CAST(DOLocationID AS STRING),
CAST(payment_type AS STRING), fare_amount, tolls_amount, tip_amount
FROM `taxi-rides-ny.nytaxi.yellow_tripdata_partitioned` WHERE fare_amount != 0
);
```

### **3️⃣ Model Training & Evaluation**
Creating a **Linear Regression model** to predict tip amounts:
```sql
CREATE OR REPLACE MODEL `taxi-rides-ny.nytaxi.tip_model`
OPTIONS (model_type='linear_reg', input_label_cols=['tip_amount'], DATA_SPLIT_METHOD='AUTO_SPLIT') AS
SELECT * FROM `taxi-rides-ny.nytaxi.yellow_tripdata_ml` WHERE tip_amount IS NOT NULL;
```

Evaluate model performance:
```sql
SELECT * FROM ML.EVALUATE(MODEL `taxi-rides-ny.nytaxi.tip_model`, (SELECT * FROM `taxi-rides-ny.nytaxi.yellow_tripdata_ml` WHERE tip_amount IS NOT NULL));
```

### **4️⃣ Prediction & Hyperparameter Tuning**
Generating predictions and explaining results:
```sql
SELECT * FROM ML.PREDICT(MODEL `taxi-rides-ny.nytaxi.tip_model`, (SELECT * FROM `taxi-rides-ny.nytaxi.yellow_tripdata_ml` WHERE tip_amount IS NOT NULL));
```

Optimizing the model using hyperparameter tuning:
```sql
CREATE OR REPLACE MODEL `taxi-rides-ny.nytaxi.tip_hyperparam_model`
OPTIONS (model_type='linear_reg', input_label_cols=['tip_amount'], DATA_SPLIT_METHOD='AUTO_SPLIT', num_trials=5, max_parallel_trials=2, l1_reg=hparam_range(0, 20), l2_reg=hparam_candidates([0, 0.1, 1, 10])) AS
SELECT * FROM `taxi-rides-ny.nytaxi.yellow_tripdata_ml` WHERE tip_amount IS NOT NULL;
```

By implementing **structured storage in PostgreSQL & BigQuery along with BigQuery ML**, this phase ensures **optimized query performance, scalable storage, and analytical readiness** for NYC Taxi data. 🚀 Next, we move to **Analytics Engineering with dbt!**

