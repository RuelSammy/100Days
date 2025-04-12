#Load and manipulate data using Pandas.
# sample_pandas_script.py

import pandas as pd

# -----------------------
# 1. Create Sample Dataset
# -----------------------

data = {
    'CustomerID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Laptop', 'Smartwatch'],
    'Quantity': [1, 2, 1, 3, 2],
    'Price': [1000, 500, 300, 1000, 200],
    'PurchaseDate': pd.to_datetime(['2023-04-01', '2023-04-03', '2023-04-04', '2023-04-10', '2023-04-12'])
}

df = pd.DataFrame(data)

# -----------------------
# 2. Explore the Dataset
# -----------------------

print("First 5 rows:\n", df.head())
print("\nDataset info:\n")
print(df.info())
print("\nSummary statistics:\n", df.describe())
print("\nColumn names:", df.columns.tolist())

# -----------------------
# 3. Add New Columns
# -----------------------

# Calculate total purchase amount
df['Total'] = df['Quantity'] * df['Price']

# -----------------------
# 4. Filter Data
# -----------------------

# Get all laptop purchases
laptop_df = df[df['Product'] == 'Laptop']
print("\nLaptop purchases:\n", laptop_df)

# -----------------------
# 5. Sort Data
# -----------------------

# Sort by total in descending order
sorted_df = df.sort_values(by='Total', ascending=False)
print("\nSorted by Total Purchase:\n", sorted_df)

# -----------------------
# 6. Grouping & Aggregation
# -----------------------

# Total sales by product
grouped = df.groupby('Product')['Total'].sum()
print("\nTotal sales by product:\n", grouped)

# -----------------------
# 7. Check for Missing Data
# -----------------------

print("\nMissing values in each column:\n", df.isnull().sum())

# -----------------------
# 8. Save to CSV (Optional)
# -----------------------

df.to_csv('sales_data.csv', index=False)
print("\nDataset saved to 'sales_data.csv'")
