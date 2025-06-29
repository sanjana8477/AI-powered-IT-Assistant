import pandas as pd

# Change these filenames as needed
excel_path = "CaseDataWithResolution.xlsx"
csv_path = "incidents.csv"

# Read the Excel file (first sheet by default)
df = pd.read_excel(excel_path)

# Save as CSV
df.to_csv(csv_path, index=False)

print(f"Saved as {csv_path}")