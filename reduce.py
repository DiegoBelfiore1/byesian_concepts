import pandas as pd
import os

# Definizione dei file di input e output
input_file = "/mnt/cimec-storage6/users/diego.belfiore/Projects/bayesian_concepts/exp_mimic/data/mimic_social_history.csv"
output_file = "exp_mimic/data/mimic_social_history_reduced.csv"

# Controlla se il file di input esiste
if not os.path.exists(input_file):
    print(f"❌ Errore: Il file {input_file} non esiste.")
    exit(1)

print(f"📥 Caricando il dataset originale da: {input_file}")

# Carica il dataset
df = pd.read_csv(input_file)

# Seleziona 50 righe casuali (se il dataset è più grande)
if len(df) > 50:
    df_reduced = df.sample(n=50, random_state=42)
    print(f"✅ Selezionate 50 righe casuali su {len(df)} totali.")
else:
    df_reduced = df
    print(f"⚠️ Il dataset ha solo {len(df)} righe. Verrà usato l'intero dataset.")

# Salva il nuovo dataset
df_reduced.to_csv(output_file, index=False)

print(f"📤 Nuovo dataset salvato in: {output_file} ({len(df_reduced)} righe)")
