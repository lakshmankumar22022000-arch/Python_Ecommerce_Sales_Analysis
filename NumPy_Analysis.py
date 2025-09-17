import pandas as pd
import numpy as np

# 1. Load Dataset

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# 2. Data Cleaning

df = df.dropna()
df['SALES'] = pd.to_numeric(df['SALES'], errors='coerce')
df = df.dropna(subset=['SALES'])

# Convert sales to NumPy array
sales_array = df['SALES'].values

# 3. Analysis

mean_sales = np.mean(sales_array)
median_sales = np.median(sales_array)
std_sales = np.std(sales_array)
total_sales = np.sum(sales_array)
max_sale = np.max(sales_array)
min_sale = np.min(sales_array)

# 4. Insights

print("\n--- NumPy Analysis ---")
print(f"Total Sales: {total_sales:,.2f}")
print(f"Average Sales: {mean_sales:,.2f}")
print(f"Median Sales: {median_sales:,.2f}")
print(f"Sales Standard Deviation: {std_sales:,.2f}")
print(f"Maximum Single Sale: {max_sale:,.2f}")
print(f"Minimum Single Sale: {min_sale:,.2f}")