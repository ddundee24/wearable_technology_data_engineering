# Wearable Technology Data Engineering

A multi-project repository focused on building data engineering pipelines for wearable technology platforms used in sports performance monitoring.

Each project in this repository covers the full pipeline from API ingestion to cloud deployment (Azure), supporting performance analytics, training load analysis, and athlete tracking.

---

## Projects

### Catapult

An ingestion and transformation pipeline for **Catapult Sports** wearable data.  
- Extracts multi-endpoint data via authenticated API calls
- Cleans and normalizes nested JSON responses
- Exports `.parquet` files for Azure Data Lake Gen2
- Structured for integration with Azure Data Factory

---

## Stack

- **Python** (pandas, requests, python-dotenv)
- **Azure Data Lake Gen2**
- **Azure Data Factory**
- **Parquet file format** for optimized cloud storage
- Structured for modular expansion (Vald)

---

## Setup Instructions

Each subproject contains:
- `.env.example` to guide API setup
- `requirements.txt` for dependencies
- `README.md` with project-specific details

To get started:

```bash
git clone https://github.com/ddundee24/wearable_technology_data_engineering.git
cd wearable_technology_data_engineering/catapult_api
```

Then follow the instructions in the subproject's README.

---

## Planned Additions

- ✅ Catapult ingestion + transformation
- 🔜 Upload automation to Azure Data Lake
- 🔜 Data validation pipeline
- 🔜 Additional integrations: Vald

---

## Maintainer

Dominic “Crocodile” Dundee  
[GitHub @ddundee24](https://github.com/ddundee24)

---

## License

MIT — free to use, modify, and share.
