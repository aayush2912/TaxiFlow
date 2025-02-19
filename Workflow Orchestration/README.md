# 🛠️ TaxiFlow: Workflow Orchestration with Kestra

## 📅 Step 2: Workflow Orchestration

This phase automates the **ETL (Extract, Transform, Load) pipeline** using **Kestra**, ensuring **data extraction, validation, transformation, and loading** into a structured warehouse. The pipeline is designed for **scalability, monitoring, and automated execution**.

---

## 🔧 Key Components

### **1️⃣ Kestra Workflow Design**
- **Extract Tasks**: Downloads raw data from **NYC TLC sources**.
- **Transform Tasks**: Cleans and structures data for analytics.
- **Load Tasks**: Stores processed data in **Google Cloud Storage (GCS) and BigQuery**.
- **Validation Tasks**: Ensures data integrity through schema checks.

### **2️⃣ Scheduling & Automation**
- **Automated monthly data ingestion**.
- **Backfilling support** for historical data.
- **Monitoring & Alerts** for failures or anomalies.

### **3️⃣ Error Handling & Recovery**
- **Retries on failure** for unstable network operations.
- **Logging and alerts** for monitoring job execution.
- **Automated recovery** from pipeline disruptions.

---

## 🚀 Workflow Implementation

### **1️⃣ Install & Configure Kestra**
Ensure Kestra is installed and running locally or on a cloud instance.

Start Kestra using Docker:
```bash
docker-compose up -d kestra
```

Check if Kestra UI is accessible at: `http://localhost:8080`

### **2️⃣ Kestra Flows Overview**
| Flow Name | Description |
|------------------------------|--------------------------------|
| `01_getting_started_data_pipeline.yaml` | Basic example pipeline to test Kestra setup. |
| `02_postgres_taxi.yaml` | Ingests NYC Taxi data into a local PostgreSQL database. |
| `02_postgres_taxi_scheduled.yaml` | Scheduled version of `02_postgres_taxi.yaml`, automating data ingestion at defined intervals. |
| `03_postgres_dbt.yaml` | Executes dbt transformations on PostgreSQL data. |
| `04_gcp_kv.yaml` | Manages key-value storage setup in GCP for pipeline configurations. |
| `05_gcp_setup.yaml` | Deploys foundational GCP resources like GCS buckets and IAM roles. |
| `06_gcp_taxi.yaml` | Ingests taxi data into Google Cloud Storage (GCS) and loads it into BigQuery. |
| `06_gcp_taxi_scheduled.yaml` | Scheduled version of `06_gcp_taxi.yaml`, automating cloud data ingestion. |
| `07_gcp_dbt.yaml` | Runs dbt transformations on BigQuery data to create structured analytics tables. |

### **3️⃣ Deploy Workflow**
Apply the workflow using:
```bash
kestra deployments apply 02_postgres_taxi.yaml
```

### **4️⃣ Execute Workflow**
Run the workflow manually:
```bash
kestra executions start data-engineering.02_postgres_taxi
```

Monitor execution via Kestra UI or CLI:
```bash
kestra executions list --namespace data-engineering
```

---

## 📅 **Automating Workflows with Scheduling**
- The **scheduled workflows** (`*_scheduled.yaml`) run on a defined interval.
- Modify scheduling by updating the **cron expression** in YAML:
```yaml
schedule:
  type: "cron"
  cron: "0 0 * * *"  # Runs every midnight
```
- Deploy the updated workflow:
```bash
kestra deployments apply 06_gcp_taxi_scheduled.yaml
```

By implementing **Kestra for orchestration**, this step ensures a **scalable, automated, and monitored** workflow for NYC Taxi data processing. The next step focuses on **data warehousing and structured storage!** 🚀

