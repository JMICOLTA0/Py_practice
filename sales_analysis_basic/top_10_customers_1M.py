# Exercise: Analyzing sales data from csv file (1000 rows-file)

# Question: Top 10 customers by revenue

import pandas as pd

# Load the data
sales = pd.read_csv('sales_retail_1M.csv')

# Calculate revenue
sales["revenue"] = sales["amount"] * sales["unit_price"]

# Sum revenue grouped by customer, sort the data by values (revenue) and get top 10
top_10_customers_rev = sales.groupby("customer")["revenue"].sum().sort_values(ascending=False).head(10)

print(f'    *** Top 10 customers ***')
for client_name, revenue in top_10_customers_rev.items():
    print(f'Name: {client_name:<10} Revenue: ${revenue:.0f}')

