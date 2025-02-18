# 🚖 TaxiFlow: Scalable NYC Taxi Data Pipeline

**A comprehensive data engineering project for processing, analyzing, and orchestrating NYC taxi data at scale using cloud-native and big data technologies.**

---

## 📌 Project Overview  
This project is designed to **ingest, process, analyze, and orchestrate NYC Taxi data from 2019 to 2021** using a scalable and automated pipeline. The goal is to enable real-time analytics, efficient batch processing, and a structured data warehouse for business intelligence use cases. The pipeline integrates **Docker, Terraform, Kestra, Spark, Kafka, and BigQuery** to ensure **performance, reliability, and automation** in handling large datasets.

---

## 🚀 Key Features  
- **Infrastructure Automation:** Provisioned cloud resources on **Google Cloud Platform (GCP)** using Terraform.  
- **Data Processing:** Implemented **PySpark and PostgreSQL** for handling large datasets efficiently.  
- **ETL Workflow Orchestration:** Used **Kestra** for **automated data extraction, transformation, and loading (ETL)** with built-in scheduling and monitoring.  
- **Data Warehousing:** Designed an optimized schema in **BigQuery** to support fast analytical queries.  
- **Analytics Engineering:** Used **dbt (Data Build Tool)** for modular **data modeling, testing, and documentation**.  
- **Batch Processing:** Leveraged **Apache Spark** on Dataproc for processing millions of taxi records.  
- **Real-time Processing:** Deployed **Kafka Streams and ksqlDB** for **live analytics and event-driven architecture**.  
- **Monitoring & Error Handling:** Integrated robust **logging, alerting, and automated recovery mechanisms** for system reliability.  

---

## 📊 Project Architecture  
```plaintext
[ NYC TLC Data ] → [ Google Cloud Storage ] → [ Processing Layer ] → [ Data Warehouse ] → [ Analytics ]
```

### **Technology Stack & Tools**  
- **Data Engineering:** Python, SQL, PySpark  
- **Cloud Services:** Google Cloud Storage, BigQuery, Dataproc  
- **Infrastructure:** Terraform, Docker  
- **Orchestration:** Kestra  
- **Batch Processing:** Apache Spark (Dataproc)  
- **Stream Processing:** Kafka, ksqlDB  
- **Analytics Engineering:** dbt  
- **Development Tools:** Git, pgAdmin  

---

## 👨‍💻 Data Pipeline Phases  
### **1️⃣ Infrastructure Setup**  
- Set up **PostgreSQL & pgAdmin** locally using **Docker**.  
- Provisioned **Google Cloud resources** (GCS, BigQuery, IAM policies) with **Terraform**.  

### **2️⃣ Workflow Orchestration with Kestra**  
- Extracts, transforms, and loads (ETL) **taxi trip records** from **NYC TLC datasets**.  
- **Automated scheduled runs & backfilling** capabilities for historical data.  
- **Monitors and alerts** for pipeline failures.  

### **3️⃣ Data Warehousing**  
- **PostgreSQL for local development**, **BigQuery for cloud storage**.  
- Implemented **partitioning, indexing, and query optimizations** to handle large datasets efficiently.  

### **4️⃣ Analytics Engineering with dbt**  
- Created **staging models, marts, and core business logic**.  
- **Ensured data quality** through **tests, documentation, and version control**.  

### **5️⃣ Batch Processing with Spark**  
- Processed **millions of taxi records** using **PySpark on Dataproc**.  
- Optimized queries and **reduced execution time** through efficient transformations.  

### **6️⃣ Real-time Processing with Kafka**  
- Deployed **Kafka Streams** to **enable live data streaming and analytics**.  
- Integrated **ksqlDB for real-time data transformations and monitoring**.  

---

## 📊 Performance Highlights  
✅ Processed **millions of NYC taxi records** with optimized batch processing.  
✅ Reduced pipeline execution time by **40%** with Spark optimizations.  
✅ Implemented **low-latency real-time analytics** using Kafka streaming.  
✅ Automated **error handling & recovery mechanisms** to enhance reliability.  

---

## 🌟 Future Enhancements  
💡 **Machine Learning Integration** – Predicting **demand forecasting, surge pricing, and traffic patterns**.  
💡 **Real-time Dashboards** – **Looker, Tableau, or Grafana** integration for business insights.  
💡 **Advanced Analytics** – Identifying **peak demand times and user behavior** trends.  
💡 **Enhanced Monitoring & Alerts** – Implementing **AI-based anomaly detection**.  

---

## 🛠️ Setup & Installation  
1️⃣ Clone the repository:  
   ```bash
   git clone https://github.com/aayush2912/TaxiFlow.git  
   cd TaxiFlow
   ```

2️⃣ Set up infrastructure:  
   ```bash
   terraform init
   terraform apply
   ```

3️⃣ Start Docker containers (PostgreSQL & pgAdmin):  
   ```bash
   docker-compose up -d
   ```

4️⃣ Run Kestra ETL pipelines:  
   ```bash
   kestra deployments apply
   ```

5️⃣ Deploy dbt models:  
   ```bash
   dbt run
   ```

---

