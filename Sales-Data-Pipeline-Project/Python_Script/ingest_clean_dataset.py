import pandas as pd

# 1. LOADING THE DATASET
# Using the cleaned CSV exported from pgAdmin
file_path = r"C:\Users\tourl\OneDrive\Υπολογιστής\2026 Portfolio Projects\1st Project\Sales Dataset\clean_sales_dataset.csv"
df = pd.read_csv(file_path)

# 2. VISUAL INSPECTION
# Checking the first 5 rows to ensure data looks correct
print("--- FIRST 5 ROWS ---")
print(df.head())

# 3. DIMENSIONS
# Confirming the total number of records (rows) and attributes (columns)
print("\n--- SHAPE (Rows, Columns) ---")
print(df.shape)

# 4. COLUMN NAMES
# Listing all available columns in the dataframe
print("\n--- COLUMN NAMES ---")
print(df.columns)

# 5. DATA TYPES
# Verifying if numbers are integers/floats and categories are objects/strings
print("\n--- DATA TYPES ---")
print(df.dtypes)

# 6. STATISTICAL SUMMARY
# Getting a quick overview of mean, min, max, and distribution for numeric columns
print("\n--- STATISTICAL DESCRIPTION ---")
print(df.describe())

# 7. NULL VALUES CHECK
# Confirming that our SQL cleaning worked and there are 0 nulls in key columns
print("\n--- NULL VALUES PER COLUMN ---")
print(df.isnull().sum())