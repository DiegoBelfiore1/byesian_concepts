import pandas as pd # type: ignore

file_path = "discharge.csv.gz"
df = pd.read_csv(file_path)
print(df.columns)
print(df.head())