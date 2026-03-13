import pandas as pd
from sqlalchemy import create_engine
import urllib.parse


user = 'postgres'
password = 'password'  # Ο κωδικός σου
host = 'localhost'
port = '5432'
db_name = 'project1_sales'

# Password Preparation
safe_password = urllib.parse.quote_plus(password)

# File Path
file_path = r"C:\Users\tourl\OneDrive\Υπολογιστής\2026 Portfolio Projects\1st Project\Sales Dataset\project1_sales.csv"

try:
    # Read CSV
    df = pd.read_csv(file_path, sep=';', encoding='latin1')
    print("File read successfully")

    # Connection with PostgreSQL
    engine = create_engine(f'postgresql://{user}:{safe_password}@{host}:{port}/{db_name}')

    # Upload in database
    df.to_sql('sales', engine, if_exists='replace', index=False)
    
    print("-" * 30)
    print("Data uploaded in SQL.")
    print(f"total rows: {len(df)}")
    print("-" * 30)

except Exception as e:
    print(f"error: {e}")