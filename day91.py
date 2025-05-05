#python for data science
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data.csv")

# Check for null values
print(df.isnull().sum())

# Drop rows with missing values
df.dropna(inplace=True)

# Fill missing values with a default
# df['column_name'].fillna("Unknown", inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Strip whitespace from string columns
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Convert column to datetime
df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')

# Standardize text (e.g., lowercase)
df['category'] = df['category'].str.lower()

print(df.head())
