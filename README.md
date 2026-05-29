# Data Governance & Metadata Management Portal

An end-to-end data governance and metadata management project built using:
- Great Expectations
- Streamlit
- Azure SQL / SQLite simulation
- Pandas
- Role-Based Access Control
- Metadata Registry
- Data Quality Validation Reports

## Features
- Automated Data Quality Validation
- Metadata Registry with lineage tracking
- Column-level profiling
- Governance Dashboard
- Role-based login simulation
- Downloadable HTML reports

## Architecture
Raw CSV -> Silver Layer -> Great Expectations -> Metadata Registry -> Streamlit Portal

## Run Locally

```bash
pip install -r requirements.txt
python setup_metadata.py
great_expectations init
streamlit run app.py
```