# 🛠️ TaxiFlow: Infrastructure Setup

## 📅 Step 1: Infrastructure Setup

The infrastructure setup phase ensures a robust and scalable environment for data ingestion, processing, and storage. This step includes configuring **PostgreSQL, pgAdmin, Docker, and Terraform** to establish a cloud-based data engineering architecture.

---

## 🔧 Infrastructure Components

### 1️⃣ **Local Development Setup (Docker)**
- **PostgreSQL**: Database for structured data storage and initial transformations.
- **pgAdmin**: Web-based GUI for PostgreSQL database management.
- **Docker**: Containerizes PostgreSQL and pgAdmin for easy deployment and scalability.
- **Python Scripts**: For data ingestion, transformation, and validation.

### 2️⃣ **Cloud Infrastructure (Terraform on GCP)**
- **Google Cloud Storage (GCS)**: Centralized storage for raw taxi data.
- **BigQuery**: Data warehouse optimized for analytical queries.
- **IAM Roles & Policies**: Secure access to cloud resources.
- **Networking Configuration**: Ensures proper connectivity across cloud components.
- **Terraform**: Automates provisioning and infrastructure management.

---

## 🛠️ Local Development Setup

### **1️⃣ Install and Run Docker Containers**

Ensure Docker is installed and running on your local machine. Then, execute the following command to start PostgreSQL and pgAdmin:

```bash
docker-compose up -d
```

This will:
- Spin up a PostgreSQL instance with persistent storage.
- Deploy pgAdmin for managing PostgreSQL.

### **2️⃣ Verify PostgreSQL Connection**
- Open `pgAdmin` at `http://localhost:8080`.
- Use the following credentials (set in `docker-compose.yml`):
  - **Username**: `admin@pgadmin.com`
  - **Password**: `admin`
- Connect PostgreSQL using:
  - **Host**: `postgres`
  - **Port**: `5432`
  - **Database**: `nyc_taxi_data`

---

## 🌐 Cloud Infrastructure Setup

### **1️⃣ Initialize Terraform**
Ensure Terraform is installed, then initialize the project:

```bash
terraform init
```

This command:
- Downloads required Terraform providers.
- Prepares Terraform for deployment.

### **2️⃣ Apply Terraform Configuration**
To provision cloud infrastructure, execute:

```bash
terraform apply
```

Terraform will:
- Create **GCS Buckets** for raw data storage.
- Set up **BigQuery datasets and tables**.
- Configure **IAM roles** to manage access.
- Establish **networking rules** for connectivity.

### **3️⃣ Verify Cloud Resources**
After deployment:
- Navigate to **Google Cloud Console** (`https://console.cloud.google.com`)
- Check **GCS Buckets** under `Storage > Browser`
- Verify **BigQuery datasets** under `BigQuery > SQL Workspace`
- Confirm **IAM roles and permissions** under `IAM & Admin`

---

## 📊 Infrastructure Validation

### **PostgreSQL Validation**
Run the following SQL command to check the database connection:

```sql
SELECT COUNT(*) FROM information_schema.tables;
```

### **Cloud Resource Validation**
Verify Terraform state:

```bash
terraform state list
```

If everything is configured correctly, your infrastructure is now ready for the next phase of the TaxiFlow project!

---

