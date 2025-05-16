# Mini-project: Analyzing sales data from csv file (1000 rows-file)

# Question 1: Total sales (amount and revenue)
# Question 2: Sales by customer
# Question 3: Most sold item by quantity
# Question 4: Count of transactions by customer
# Question 5: Grouped sales by customer and product

import pandas as pd
from time import perf_counter

start_time = perf_counter()
sales = pd.read_csv('sales_retail_1M.csv')

sales = sales.to_dict(orient="records")

# Question 1: Total sales (units)
total_units = 0

for sale in sales:
    total_units += sale['amount']

print(f'*** Total sales ***\n -Total units sold = {total_units}')

# Question 1: Total sales (revenue)
total_rev = 0

for sale in sales:
    total_rev += sale['amount'] * sale['unit_price']

print(f' -Total revenue: ${total_rev:.0f}\n')


# Question 2: Sales by customer

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


# Question 3: Most sold item by quantity

most_sold_prods = {}
most_sold_itm = None
max_quant = 0

for sale in sales:
    product = sale['product']
    amount = sale['amount']

    if product not in most_sold_prods:
        most_sold_prods[product] = amount
    else:
        most_sold_prods[product] += amount

for prod, qnt in most_sold_prods.items():
    if qnt > max_quant:
        max_quant = qnt
        most_sold_itm = prod

print(f'*** Most sold item by quantity ***\n  The most sold product by quantity is: {most_sold_itm} with {max_quant} units\n')


# Question 4: Count of transactions by customer

count_transx = {}

for sale in sales:
    clt = sale['customer']

    if clt not in count_transx:
        count_transx[clt] = 1
    else:
        count_transx[clt] +=1

print('*** Transactions count by customer ***')
for cl, cnt in count_transx.items():
    print(f' --> Client name: {cl:<8} Num_transx: {cnt}')

print()


# Question 5: Grouped sales by customer and product

grouped_sales ={}

for sale in sales:
    client_name = sale['customer']
    product = sale['product']
    revenue = sale['amount'] * sale['unit_price']

    if client_name not in grouped_sales:
        grouped_sales[client_name] = {}
    if product not in grouped_sales[client_name]:
        grouped_sales[client_name][product] = revenue
    else:
        grouped_sales[client_name][product] += revenue

print('*** Grouped revenue by customer and product ***')
for client, products in grouped_sales.items():
    print(f' -> Customer: {client}')
    for prod, rev in products.items():
        print(f' --> Item: {prod:<10} --> Revenue: ${rev:.0f}')

print()

end_time = perf_counter()
run_time = end_time - start_time
print(f'Total runtime: {run_time}')








