import pandas as pd

# Load patient data
data = pd.read_csv("data/patients.csv")

# Show the first rows
print("Patient Data Preview:")
print(data.head())

