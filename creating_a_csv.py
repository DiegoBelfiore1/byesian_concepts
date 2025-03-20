import pandas as pd
import os

# Percorsi dei file (aggiorna con i tuoi percorsi reali)
mapping_notes_path = "/mnt/cimec-storage6/users/diego.belfiore/Projects/bayesian_concepts/exp_mimic/data/mapping_notes.csv"
discharge_path = "discharge.csv.gz"
output_path = "merged_dataset.csv"

# 1. Carica i dataset
df1 = pd.read_csv(mapping_notes_path)  # contiene 'row_id'
df2 = pd.read_csv(discharge_path, compression='gzip')  # contiene 'text'

# 2. Controlla e uniforma i tipi di dato
#    Assicurati che row_id sia numerico e che text sia stringa
df1['row_id'] = pd.to_numeric(df1['row_id'], errors='coerce')
df2['text'] = df2['text'].astype(str)

# 3. Resetta l’indice di df2 per assicurarti che il nuovo indice vada da 0 a len(df2)-1
df2.reset_index(drop=True, inplace=True)

# 4. Filtro: rimuovi eventuali row_id fuori range [0, len(df2)-1]
df1 = df1[df1['row_id'].between(0, len(df2) - 1)]

# 5. Inserisci la colonna 'text' di df2 corrispondente al row_id
df1['text'] = df1['row_id'].apply(lambda x: df2.loc[x, 'text'] 
                                              if 0 <= x < len(df2) 
                                              else None)

# 6. Salva il risultato in un nuovo CSV
if not df1.empty:
    df1.to_csv(output_path, index=False)
    print(f"Dataset salvato con successo in: {os.path.abspath(output_path)}")
else:
    print("ERRORE: Il DataFrame risultante è vuoto, nessun file salvato.")

# 7. (Opzionale) Visualizza un’anteprima
print(df1.head())
