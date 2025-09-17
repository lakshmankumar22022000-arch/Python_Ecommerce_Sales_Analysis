import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# 2. Data Cleaning

df = df.dropna()
df["SALES"] = pd.to_numeric(df["SALES"], errors="coerce")
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")
df = df.dropna(subset=["ORDERDATE", "SALES"])

# 3. Sales by Product Line

product_sales = df.groupby("PRODUCTLINE")["SALES"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
plt.bar(product_sales.index, product_sales.values, color="skyblue")
plt.title("Total Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n--- Insights: Product Line ---")
print(product_sales.head(3))

# 4. Monthly Sales Trend

monthly_sales = df.groupby(df["ORDERDATE"].dt.to_period("M"))["SALES"].sum()
monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o", color="green")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

print("\n--- Insights: Monthly Sales Trend ---")
print("Best Month for Sales:", monthly_sales.sort_values(ascending=False).index[0])

# 5. Sales by Region (Territory)

if "TERRITORY" in df.columns:
    region_sales = df.groupby("TERRITORY")["SALES"].sum().sort_values(ascending=False)

    plt.figure(figsize=(8,5))
    plt.bar(region_sales.index, region_sales.values, color="coral")
    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()

    print("\n--- Insights: Region ---")
    print("Top Region by Sales:", region_sales.index[0])