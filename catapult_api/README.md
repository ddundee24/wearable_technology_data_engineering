# Catapult Data Pipeline

This project ingests athlete and performance data from the **Catapult Sports API**, cleans it using Python, and uploads it to **Azure Data Lake Gen2** for further processing via **Azure Data Factory**.

---

## Features

- Authenticated API ingestion
- Multi-endpoint data extraction
- Nested JSON flattening
- Data cleaning and standardization
- Upload to Azure Data Lake Gen2
- Compatible with Azure Data Factory pipelines

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ddundee24/wearable_technology_data_engineering.git
cd wearable_technology_data_engineering/catapult
```

### 2. Set Up Your Environment

Create a `.env` file in this directory by copying the template:

```bash
cp .env.example .env
```

Fill in your real API credentials in the `.env` file.

### 3. Install Python Requirements

```bash
pip install -r requirements.txt
```

---

## Running the Pipeline

Run the script to pull, clean, and upload data:

```bash
python api_ingestion.py
```

---

## Output Structure in Azure

Your data will be organized like this in Azure Data Lake:

```
catapult/
├── athletes.parquet
├── thresholds.parquet
└── workouts.parquet
```

These files can be consumed by Azure Data Factory pipelines.

---

## Environment Variables

Defined in `.env` (example provided in `.env.example`):

- `token`: your Catapult API token
- `base_url`: Catapult API base URL (e.g. `https://connect-us.catapultsports.com/api/v6/`)

---

## License

MIT — free to use, modify, and share.

---

## Maintainer

Dominic “Crocodile” Dundee  
[@ddundee24](https://github.com/ddundee24)