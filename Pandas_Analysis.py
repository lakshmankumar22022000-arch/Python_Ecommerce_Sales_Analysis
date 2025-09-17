import pandas as pd

# 1. Load Dataset

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# 2. Data Cleaning

df = df.dropna()
df['SALES'] = pd.to_numeric(df['SALES'], errors='coerce')
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')
df = df.dropna(subset=['ORDERDATE', 'SALES'])

# 3. Analysis
# Top 5 products by revenue
top_products = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)

# Monthly sales trend
monthly_sales = df.groupby(df['ORDERDATE'].dt.to_period('M'))['SALES'].sum()

# Sales by region
if 'TERRITORY' in df.columns:
    region_sales = df.groupby('TERRITORY')['SALES'].sum().sort_values(ascending=False)

# 4. Insights

print("\n--- Pandas Analysis: Top Products ---")
print(top_products.head(5))

print("\n--- Pandas Analysis: Monthly Sales Trend ---")
print(monthly_sales.head(5))

if 'TERRITORY' in df.columns:
    print("\n--- Pandas Analysis: Sales by Region ---")
    print(region_sales.head(5))