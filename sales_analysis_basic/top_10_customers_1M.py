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



# Top 3 products per customer (Code 100% from ChatGPT, added using Working with Apps feature)
# Prompt: I want to find the top 3 products bought per customer using a similar approach I used for the top 10 customers. Do it by yourself. You've been granted permissions to modify the file
print('\n    *** Top 3 products per customer ***')
top_products = (
    sales.groupby(["customer", "product"])["revenue"]
    .sum()
    .reset_index()
)

top_3_products_per_customer = (
    top_products.sort_values(["customer", "revenue"], ascending=[True, False])
    .groupby("customer")
    .head(3)
)

for customer, group in top_3_products_per_customer.groupby("customer"):
    print(f'Customer: {customer}')
    for _, row in group.iterrows():
        print(f'    Product: {row["product"]:<15} Revenue: ${row["revenue"]:.0f}')

