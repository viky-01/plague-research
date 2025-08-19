from datasets import load_dataset
import pandas as pd

# Step 1: Load the dataset from Hugging Face
print("🔄 Downloading dataset from Hugging Face...")
dataset = load_dataset("DaniilOr/CoDET-M4")

# Step 2: Convert the 'train' split to pandas DataFrame
print("📦 Converting to pandas DataFrame...")
df = dataset["train"].to_pandas()

# Step 3: Show some basic info
print("\n✅ Dataset Loaded Successfully!")
print(f"Total rows: {len(df)}")
print("Available columns:", df.columns.tolist())

# Step 4: Filter human and AI code
df_human = df[df["target"] == "human"]
df_ai = df[df["target"] == "machine"]

# Step 5: Save full and filtered datasets as CSV
print("💾 Saving files...")
df.to_csv("codet_m4_full.csv", index=False)
df_human.to_csv("codet_m4_human.csv", index=False)
df_ai.to_csv("codet_m4_ai.csv", index=False)

print("\n🎉 Done! Files saved:")
print(" - codet_m4_full.csv")
print(" - codet_m4_human.csv")
print(" - codet_m4_ai.csv")
