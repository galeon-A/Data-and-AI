import sqlite3
import pandas as pd
from pathlib import Path

Path("metadata").mkdir(exist_ok=True)

conn = sqlite3.connect("metadata/metadata.db")

metadata = pd.DataFrame([
    {
        "table_name": "sales_data",
        "owner": "Data Engineering",
        "refresh_frequency": "Daily",
        "column_descriptions": "Sales transactions and customer revenue metrics",
        "dq_pass_rate": "98%",
        "lineage": "Raw CSV -> Silver Layer -> Governance Portal"
    }
])

metadata.to_sql("metadata_registry", conn, if_exists="replace", index=False)

print("Metadata registry created successfully.")