# ============================================================
# ETL pipeline
# ============================================================
import pandas as pd
import sqlite3
from datetime import datetime

def extract():
    print("Extracting...")
    df = pd.read_csv('/Users/tejas_borse/Downloads/Sample - Superstore.csv', encoding='latin1')
    return df

def transform(df):
    print("Transforming...")
    df['Order Date']      = pd.to_datetime(df['Order Date'])
    df['Ship Date']       = pd.to_datetime(df['Ship Date'])
    df['Month']           = df['Order Date'].dt.to_period('M').astype(str)
    df['profit_margin']   = (df['Profit'] / df['Sales'] * 100).round(2)
    df['is_profitable']   = df['Profit'] > 0
    df['days_to_ship']    = (df['Ship Date'] - df['Order Date']).dt.days
    df.columns            = df.columns.str.lower().str.replace(' ', '_')
    df                    = df.dropna(subset=['sales', 'profit'])
    return df

def load(df):
    print("Loading...")
    conn = sqlite3.connect('superstore_cleaned.db')
    df.to_sql('orders_clean', conn, if_exists='replace', index=False)
    conn.close()
    print(f"Pipeline complete. {len(df)} rows loaded into superstore_cleaned.db")

# Run the pipeline
df_raw = extract()
df_clean = transform(df_raw)
load(df_clean)