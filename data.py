import pandas as pd
import os

# Step 1: Read the CSV
df = pd.read_csv("codet_m4_full.csv")

# Step 2: Clean rows with missing or float code
df = df[df["code"].notnull()]  # Remove NaN
df = df[df["code"].apply(lambda x: isinstance(x, str))]  # Only keep strings

# Step 3: Define root output folder
root_dir = "code_snippets"
os.makedirs(root_dir, exist_ok=True)

# Step 4: Loop and save code per language
for idx, row in df.iterrows():
    code = row["code"]
    lang = str(row["language"]).lower()
    target = row["target"]

    # Choose file extension
    ext = "txt"
    if lang == "python":
        ext = "py"
    elif lang == "java":
        ext = "java"
    elif lang in ["cpp", "c++"]:
        ext = "cpp"

    # Subfolder by language
    lang_dir = os.path.join(root_dir, lang)
    os.makedirs(lang_dir, exist_ok=True)

    # Create file
    filename = f"{target}_{idx}.{ext}"
    filepath = os.path.join(lang_dir, filename)

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(code))  # Ensure it's a string
    except Exception as e:
        print(f"❌ Error writing {filename}: {e}")

print(f"✅ Done! Files stored in: {root_dir}/language/")
