# Python_Ecommerce_Sales_Analysis
## About the Project

This project demonstrates **Sales Data Analysis** using Python.
It includes **data cleaning, analysis, and visualization** using `pandas`, `NumPy`, `matplotlib`, and `seaborn`.

---

## Dataset

* Dataset file: `sales_data_sample.csv`
* Contains sales transactions including:

  * Order Date
  * Product Line
  * Territory
  * Sales
* Encoding: `latin1`

---

## Tools & Libraries

* **Python 3.x**
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical calculations
* **Matplotlib** – Basic visualizations
* **Seaborn** – Advanced visualizations

---

## Project Workflow

1. **Data Loading**

```python
import pandas as pd
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
```

2. **Data Cleaning**

* Remove missing values
* Convert `SALES` to numeric
* Convert `ORDERDATE` to datetime

3. **Analysis**

* **Pandas:** Top products, monthly sales trends, sales by region
* **NumPy:** Total, average, median, max, min, and standard deviation of sales
* **Matplotlib & Seaborn:** Visualizations of sales trends and comparisons

---

## Key Insights

* Top performing product lines
* Peak sales months
* Regions generating highest revenue
* Statistical metrics of sales (total, average, max, min, standard deviation)

---

## 📊 Visualizations

### Total Sales by Product Line
[[Matplotlib](<img width="800" height="500" alt="Matplotlib (Bar Plot)-Total Sales by Product Line" src="https://github.com/user-attachments/assets/f7154fdc-e2f5-48b4-95d1-51923bb3002a" />)
[[Seaborn](<img width="800" height="500" alt="Seaborn (Bar Plot)-Sales by Product Line" src="https://github.com/user-attachments/assets/6c42b9b6-c36e-47f0-9c0e-8a0058714f0f" />)

