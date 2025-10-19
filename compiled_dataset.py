import pandas as pd
import os

# folder_path = "data"

# compiled = []

# csv_files = [f for f  in os.listdir(folder_path) if f.endswith('.csv')]

# for file in csv_files:
#     df = pd.read_csv(os.path.join(folder_path, file))
#     compiled.append(df)
#     print(f"Loaded: {file} with {len(df)} rows")

# compiled_df = pd.concat(compiled, ignore_index=True)

# output_file = os.path.join(folder_path, "compiled_dataset.csv")
# compiled_df.to_csv(output_file, index=False)

# print(f"\n Merged CSV saved as: {output_file}")

df = pd.read_csv("compiled_dataset.csv")

print(df.head(100))