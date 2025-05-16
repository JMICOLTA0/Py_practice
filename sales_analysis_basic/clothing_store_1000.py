# Mini-project: Analyzing sales data from csv file (1000 rows-file)


# Question 1: Total sales (amount and revenue)
# Question 2: Sales by customer
# Question 3: Most sold item by quantity
# Question 4: Count of transactions by customer
# Question 5: Grouped sales by customer and product

import pandas as pd

sales = pd.read_csv('sales_clothing.csv') # reads the csv file as a Pandas DataFrame: it behaves like a table

# print(sales.head()) print the first n rows, default = 5.
sales = sales.to_dict(orient="records") *1 # convert the DataFrame into a list of dicts (We can repeat the dataset *n times for measurements porpoises)

# Question 1: Total sales (units)
total_units = 0

for sale in sales:
    total_units += sale['amount']

print('*** Total sales ***')
print(f' -Total units sold = {total_units}')

# Question 1: Total sales (revenue)
revenue = 0

for sale in sales:
    revenue += sale['amount'] * sale['unit_price']

print(f' -Total revenue: ${revenue:.0f}\n')

# Question 2: Sales by customer
revenue_per_customer = {}

for sale in sales:
    client = sale['customer']
    revenue = sale['amount'] * sale['unit_price']

    if client not in revenue_per_customer:
        revenue_per_customer[client] = revenue
    else:
        revenue_per_customer[client] += revenue

print('*** Sales by customer ***')
for cl, rev in revenue_per_customer.items():
    print(f'-> Client: {cl:<10} Sales: ${rev:.0f}' )
print()

# Question 3: Most sold item by quantity
most_sold_p = {}
max_quantity = 0
most_sold_item = None

for sale in sales:
    product_name = sale['product']
    ordered_units = sale['amount']

    if product_name not in most_sold_p:
        most_sold_p[product_name] = ordered_units

    else:
        most_sold_p[product_name] += ordered_units

for prod, quant in most_sold_p.items():
    if quant > max_quantity:
        max_quantity = quant
        most_sold_item = prod

print('*** Most sold product by quantity ***')
print(f'Product name = {most_sold_item}, Units sold = {max_quantity}\n')

# Question 4: Count of transactions by customer
transaction_count = {}

for sale in sales:
    client_name = sale['customer']

    if client_name not in transaction_count:
        transaction_count[client_name] = 1
    else:
        transaction_count[client_name] += 1

print('*** Transactions count by customer ***')
for cl_name, count in transaction_count.items():
    print(f'The client {cl_name:<7} has made {count} transactions')
print()

# Question 5: Grouped sales by customer and product
grpd_sales = {}

for sale in sales:
    client = sale['customer']
    product = sale['product']
    revenue = sale['amount'] * sale['unit_price']

    if client not in grpd_sales:
        grpd_sales[client] = {}
    if product not in grpd_sales[client]:
        grpd_sales[client][product] = revenue
    else:
        grpd_sales[client][product] += revenue

print(f'*** Grouped sales by customer and product ***')
for customer, products in grpd_sales.items():
    print(f' -> Client: {customer}')
    for p_name, rev in products.items():
        print(f'    --> Product: {p_name:<10} Revenue: ${rev:.0f}')














