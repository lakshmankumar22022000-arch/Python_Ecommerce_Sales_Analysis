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

## Visualizations

- For a full downloadable version of the Matplotlib and Seaborn, click here:
- [Download PDF](https://github.com/lakshmankumar22022000-arch/Python_Ecommerce_Sales_Analysis/blob/main/Matplotlib%2C%20Seaborn%20Visualization.pdf)



