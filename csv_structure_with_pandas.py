import pandas as pd # type: ignore

file_path = "exp_cub_birds_existing/_output/class_1_2_3/meta-llama/Meta-Llama-3.1-8B-Instruct/concept_extractions.csv"

df = pd.read_csv(file_path)
print(df.columns)
print(df.head())