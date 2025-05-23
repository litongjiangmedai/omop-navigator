import pandas as pd

def load_concepts(path):
    df = pd.read_csv(path)
    return {row["concept_name"].lower(): row["concept_id"] for _, row in df.iterrows()}
