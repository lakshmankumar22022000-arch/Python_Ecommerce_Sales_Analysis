import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Dataset

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# 2. Data Cleaning

df = df.dropna()
df["SALES"] = pd.to_numeric(df["SALES"], errors="coerce")
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")
df = df.dropna(subset=["ORDERDATE", "SALES"])

# 3. Sales by Product Line

product_sales = df.groupby("PRODUCTLINE")["SALES"].sum().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(x="PRODUCTLINE", y="SALES", data=product_sales, palette="Blues_d")
plt.title("Total Sales by Product Line")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n--- Insights: Product Line ---")
print(product_sales.sort_values("SALES", ascending=False).head(3))

# 4. Monthly Sales Trend

monthly_sales = df.groupby(df["ORDERDATE"].dt.to_period("M"))["SALES"].sum().reset_index()
monthly_sales["ORDERDATE"] = monthly_sales["ORDERDATE"].astype(str)

plt.figure(figsize=(10,5))
sns.lineplot(x="ORDERDATE", y="SALES", data=monthly_sales, marker="o")
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n--- Insights: Monthly Sales Trend ---")
print("Best Month for Sales:", monthly_sales.sort_values("SALES", ascending=False).iloc[0,0])

# 5. Sales by Region (Territory)

if "TERRITORY" in df.columns:
    region_sales = df.groupby("TERRITORY")["SALES"].sum().reset_index()

    plt.figure(figsize=(8,5))
    sns.barplot(x="TERRITORY", y="SALES", data=region_sales, palette="coolwarm")
    plt.title("Sales by Region")
    plt.tight_layout()
    plt.show()

    print("\n--- Insights: Region ---")
    print("Top Region by Sales:", region_sales.sort_values("SALES", ascending=False).iloc[0,0])