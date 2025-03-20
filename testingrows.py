import pandas as pd

# Ricarichiamo i dataset
labelled_file = "exp_mimic/_output/long_notes/max_obs_-1/seed_0/high_snr_4/replicate_seed_2/labelled_data.csv"
concepts_file = "exp_mimic/_output/long_notes/max_obs_-1/seed_0/meta-llama/Meta-Llama-3.1-8B-Instruct/concept_extractions.csv"

df_labelled = pd.read_csv(labelled_file)
df_concepts = pd.read_csv(concepts_file)

# Ordiniamo per row_id per essere sicuri di confrontare le righe giuste
df_labelled = df_labelled.sort_values(by="row_id").reset_index(drop=True)
df_concepts = df_concepts.sort_values(by="row_id").reset_index(drop=True)

# Confrontiamo sentence
diff_sentences = df_labelled.sentence.compare(df_concepts.sentence)
print("==== DIFFERENZE TRA SENTENCE ====")
print(diff_sentences)

print("Tipo di sentence in labelled_data.csv:", df_labelled.sentence.dtype)
print("Tipo di sentence in concept_extractions.csv:", df_concepts.sentence.dtype)
print("Numero di frasi in labelled:", df_labelled['sentence'].count())
print("Numero di frasi in concepts:", df_concepts['sentence'].count())

