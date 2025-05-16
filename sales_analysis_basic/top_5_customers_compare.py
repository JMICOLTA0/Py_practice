# Exercise: Analyzing sales data from csv file (1000 rows-file)

# Question 1: Sales by customer
# Question 2: Top 5 customers by revenue

import pandas as pd
# Question 1: Sales by customer  - Using for loops

sales = pd.read_csv('sales_retail_1M.csv')

sales = sales.to_dict(orient="records")

sales_by_customer = {}

for sale in sales:
    customer = sale['customer']
    revenue = sale['amount'] * sale['unit_price']

    if customer not in sales_by_customer:
        sales_by_customer[customer] = revenue
    else:
        sales_by_customer[customer] += revenue

print('*** Sales by customer ***')
for cust, rev in sales_by_customer.items():
    print(f' -> Client name: {cust:<10} Revenue: ${rev:.0f}')

print()


# Question 2: Top 5 customers by revenue  - Using Pandas dataframes

df = pd.read_csv("sales_retail_1M.csv") # load the data

df["revenue"] = df["amount"] * df["unit_price"] # Calculate revenue per row

customer_revenue = df.groupby("customer")["revenue"].sum() # Group by customer and sum revenue

customer_revenue_sorted = customer_revenue.sort_values(ascending=False) # Sort in descending order

top_5_customers = customer_revenue_sorted.head(5) # Get top 5

# we can chain the last 3 operations like this:
customer_revenue = df.groupby("customer")["revenue"].sum().sort_values(ascending=False).head(5) # Group by customer, sum grouped revenue, sort by values in desc order and get top 5

print('*** Top 5 customers by revenue - Pandas dataframes ***')
for client, revenue in top_5_customers.items(): # A Pandas Series behaves like a Python dict when iterating over it (index, value)
    print(f' -> Client name: {client:<10} Revenue: ${revenue:.0f}')