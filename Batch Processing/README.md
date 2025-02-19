# 🛠️ TaxiFlow: Batch Processing with Apache Spark

## 📅 Step 5: Batch Processing

This phase focuses on **processing large-scale NYC Taxi data using Apache Spark**, leveraging **Google Dataproc** for cloud-based distributed computing. The goal is to **optimize query performance, enable parallel processing, and efficiently transform massive datasets**.

---

## 🔧 Key Components

### **1️⃣ Apache Spark Setup**
- **Local Spark Setup** for development and testing.
- **Google Dataproc Cluster** for scalable processing.
- **PySpark-based transformations** to process taxi trip data.

### **2️⃣ Data Processing & Transformations**
- **Schema Definition & Data Loading** from Google Cloud Storage.
- **Filtering & Cleaning** of raw taxi trip data.
- **Feature Engineering** for analytics and reporting.

### **3️⃣ Performance Optimization**
- **Partitioning & Bucketing** to enhance query performance.
- **Efficient Spark DataFrame Operations**.
- **Memory & Computation Optimization** with caching and parallelism.

---

## 🚀 Apache Spark Implementation

### **1️⃣ Running Spark Locally**
Ensure Spark is installed and running:
```bash
pyspark --master local[*]
```

### **2️⃣ Loading Taxi Data into Spark**
Example PySpark script (`load_taxi_data.py`):
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("NYC Taxi Data Processing").getOrCreate()

df = spark.read.parquet("gs://nyc-taxi-data/raw/yellow_tripdata.parquet")
df.show(5)
```

### **3️⃣ Data Transformation in PySpark**
Perform key transformations:
```python
from pyspark.sql.functions import col, when

df_cleaned = df.filter(col("fare_amount") > 0)
df_cleaned = df_cleaned.withColumn("trip_category", when(col("trip_distance") > 5, "Long").otherwise("Short"))
```

### **4️⃣ Writing Processed Data to Cloud Storage**
Save cleaned data for further analysis:
```python
df_cleaned.write.mode("overwrite").parquet("gs://nyc-taxi-data/processed/yellow_tripdata_cleaned.parquet")
```

---

## ☁️ Google Dataproc Implementation

### **1️⃣ Creating a Dataproc Cluster**
Run the following command to create a cluster:
```bash
gcloud dataproc clusters create taxi-cluster \
    --region us-central1 \
    --zone us-central1-a \
    --single-node \
    --master-machine-type n1-standard-4 \
    --image-version 2.0-debian10
```

### **2️⃣ Submitting a PySpark Job to Dataproc**
Upload the `load_taxi_data.py` script to GCS and submit it:
```bash
gcloud dataproc jobs submit pyspark gs://nyc-taxi-scripts/load_taxi_data.py \
    --cluster=taxi-cluster \
    --region=us-central1
```

### **3️⃣ Monitoring Spark Jobs**
Monitor the execution through Dataproc’s web UI or using:
```bash
gcloud dataproc jobs list --region=us-central1
```

---

## 📊 Performance Optimization

### **1️⃣ Partitioning for Faster Queries**
Partition data by pickup date for improved query efficiency:
```python
df_cleaned.write.partitionBy("pickup_date").parquet("gs://nyc-taxi-data/processed/yellow_tripdata_partitioned.parquet")
```

### **2️⃣ Caching & Persistence**
Use caching to speed up iterative computations:
```python
df_cleaned.cache()
```

### **3️⃣ Parallel Processing with Repartitioning**
Optimize parallelism for distributed processing:
```python
df_cleaned = df_cleaned.repartition(10)
```

By implementing **batch processing with Apache Spark and Dataproc**, this phase ensures **efficient, scalable, and high-performance data transformation** for NYC Taxi data analysis. 🚀 Next, we move to **Real-Time Stream Processing!**

