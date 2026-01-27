import pandas as pd

# Load patient data
data = pd.read_csv("data/patients.csv")

# Remove duplicates
data = data.drop_duplicates()

# Fill missing values
data = data.fillna(0)

# Preview
print("Cleaned Patient Data:")
print(data.head())
