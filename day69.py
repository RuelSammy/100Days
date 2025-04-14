import pandas as pd
import numpy as np
from scipy import stats

# Set seed for reproducibility
np.random.seed(42)

# Generate synthetic dataset
n = 100
data = pd.DataFrame({
    'Age': np.random.normal(35, 10, n).astype(int),
    'AnnualIncome': np.random.normal(50000, 15000, n).astype(int),
    'SpendingScore': np.random.randint(1, 101, n),
    'Gender': np.random.choice(['Male', 'Female'], n),
    'PurchasedLastMonth': np.random.choice([0, 1], n, p=[0.3, 0.7])
})

# Print raw data head
print("Preview of Data:")
print(data.head(), "\n")

# Numerical statistics
print("Basic Statistical Analysis:\n")
for col in ['Age', 'AnnualIncome', 'SpendingScore']:
    print(f"{col}:")
    print(f"  Mean: {data[col].mean():.2f}")
    print(f"  Median: {data[col].median():.2f}")
    print(f"  Mode: {data[col].mode()[0]}")
    print(f"  Standard Deviation: {data[col].std():.2f}")
    print()

# Categorical distributions
print("Gender Distribution:\n", data['Gender'].value_counts(), "\n")
print("Purchase Last Month Distribution:\n", data['PurchasedLastMonth'].value_counts(), "\n")
