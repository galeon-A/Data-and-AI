import pandas as pd
from pathlib import Path

Path("profiles").mkdir(exist_ok=True)

df = pd.read_csv("data/sales_data.csv")

profile = pd.DataFrame({
    "column": df.columns,
    "dtype": [str(df[col].dtype) for col in df.columns],
    "null_count": [df[col].isnull().sum() for col in df.columns],
    "unique_values": [df[col].nunique() for col in df.columns]
})

profile.to_csv("profiles/sales_data_profile.csv", index=False)

print("Column profile generated.")