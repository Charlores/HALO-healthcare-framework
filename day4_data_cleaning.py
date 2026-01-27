import pandas as pd

# Load patient data
data = pd.read_csv("data/patients.csv")

# Remove duplicate rows
data = data.drop_duplicates()

# Fill missing values (if any) with 0
data = data.fillna(0)

# Preview cleaned data
print("Cleaned Patient Data:")
print(data.head())
