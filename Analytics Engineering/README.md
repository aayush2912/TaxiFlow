# 🛠️ TaxiFlow: Analytics Engineering with dbt

## 📅 Step 4: Analytics Engineering

This phase focuses on **transforming and structuring raw taxi trip data** using **dbt (Data Build Tool)** for analytics and reporting. The goal is to create **clean, well-structured, and reusable data models** to power insights and decision-making.

---

## 🔧 Key Components

### **1️⃣ dbt Project Setup**
- **Folder Structure & Configuration** for dbt project.
- **Staging Models** to standardize raw data.
- **Core Models** to build analytical views.
- **Data Mart Models** for business consumption.
- **Containerized Setup** using **Docker** and **Docker Compose**.

### **2️⃣ Data Transformation & Modeling**
- **Cleaning & Standardization** of taxi trip data.
- **Feature Engineering** for analytics.
- **Incremental Models** to optimize performance.

### **3️⃣ Data Quality & Validation**
- **Testing & Assertions** to ensure data integrity.
- **Data Documentation** for transparency.
- **Version Control** for model tracking.

---

## 🚀 dbt Implementation

### **1️⃣ Setting Up dbt**
Ensure dbt is installed and initialize a new project:
```bash
dbt init taxi_flow_project
```

### **2️⃣ Configure dbt for BigQuery**
Edit `profiles.yml` to set up dbt connection:
```yaml
taxi_flow_project:
  target: dev
  outputs:
    dev:
      type: bigquery
      method: service-account
      project: taxi-rides-ny
      dataset: analytics
      threads: 4
      timeout_seconds: 300
      location: US
```

### **3️⃣ Staging Models**
Create staging models to clean and standardize raw taxi data.
Example (`models/staging/stg_taxi_trips.sql`):
```sql
WITH source AS (
    SELECT * FROM `taxi-rides-ny.nytaxi.yellow_tripdata_partitioned`
)
SELECT 
    trip_id, 
    pickup_datetime, 
    dropoff_datetime, 
    passenger_count, 
    trip_distance, 
    fare_amount, 
    total_amount, 
    payment_type
FROM source
WHERE fare_amount > 0;
```

### **4️⃣ Core Models**
Transform staging data into structured analytics tables.
Example (`models/core/taxi_trips_core.sql`):
```sql
WITH trips AS (
    SELECT * FROM {{ ref('stg_taxi_trips') }}
)
SELECT 
    trip_id, 
    pickup_datetime, 
    dropoff_datetime, 
    passenger_count, 
    trip_distance,
    fare_amount, 
    total_amount, 
    payment_type, 
    TIMESTAMP_DIFF(dropoff_datetime, pickup_datetime, SECOND) AS trip_duration_seconds
FROM trips;
```

### **5️⃣ Data Mart Models**
Create final reporting tables for BI tools.
Example (`models/marts/trip_summary.sql`):
```sql
WITH trips AS (
    SELECT * FROM {{ ref('taxi_trips_core') }}
)
SELECT 
    DATE(pickup_datetime) AS trip_date, 
    COUNT(trip_id) AS total_trips,
    AVG(trip_distance) AS avg_trip_distance, 
    AVG(fare_amount) AS avg_fare_amount
FROM trips
GROUP BY trip_date;
```

---

## 🛠️ Dockerized Setup for dbt

### **1️⃣ Dockerfile for dbt**
Create a `Dockerfile` to containerize dbt:
```dockerfile
FROM ghcr.io/dbt-labs/dbt-bigquery:latest
WORKDIR /dbt
COPY . .
RUN pip install --upgrade dbt-bigquery
ENTRYPOINT ["dbt"]
```

### **2️⃣ docker-compose.yaml**
Define a `docker-compose.yaml` file to orchestrate the dbt container:
```yaml
version: '3.8'
services:
  dbt:
    build: .
    container_name: dbt_container
    volumes:
      - .:/dbt
    environment:
      DBT_PROFILES_DIR: /dbt
    command: ["run"]
```

### **3️⃣ Running dbt in Docker**
Build and run the containerized dbt setup:
```bash
docker-compose up --build
```

Execute dbt commands within the container:
```bash
docker exec -it dbt_container dbt debug
```

---

## 📊 Data Quality & Testing

### **1️⃣ Data Testing**
Define tests in `schema.yml` to ensure data integrity:
```yaml
version: '3'
services:
  dbt-bq-dtc:
    build:
      context: .
      target: dbt-bigquery
    image: dbt/bigquery
    volumes:
      - .:/usr/app
      - ~/.dbt/:/root/.dbt/
      - ~/.google/credentials/google_credentials.json:/.google/credentials/google_credentials.json
    network_mode: host
```
Run tests using:
```bash
dbt test
```

### **2️⃣ Data Documentation**
Generate project documentation:
```bash
dbt docs generate
```
View documentation locally:
```bash
dbt docs serve
```

### **3️⃣ Incremental Model Implementation**
Optimize performance by processing only new data:
```sql
{{ config(
    materialized='incremental',
    unique_key='trip_id'
) }}
SELECT * FROM {{ ref('stg_taxi_trips') }}
{% if is_incremental() %}
WHERE pickup_datetime > (SELECT MAX(pickup_datetime) FROM {{ this }})
{% endif %}
```

By implementing **structured transformations using dbt** and containerizing the workflow with **Docker**, this phase ensures **clean, scalable, and analytics-ready data** for NYC Taxi analysis. 🚀 Next, we move to **Batch & Stream Processing!**

