# Mini-project: Analyzing sales data

# Question 1: Total sales (amount and revenue)
# Question 2: Sales by customer
# Question 3: Most sold item by quantity
# Question 4: Count of transactions by customer
# Question 5: Grouped sales by customer and product

sales = [
    {'customer': 'Fiona', 'product': 'T-shirt', 'amount': 1, 'unit_price': 15.0},
    {'customer': 'Fiona', 'product': 'Sneakers', 'amount': 1, 'unit_price': 50.0},
    {'customer': 'Bob', 'product': 'T-shirt', 'amount': 1, 'unit_price': 15.0},
    {'customer': 'Diana', 'product': 'Sneakers', 'amount': 1, 'unit_price': 50.0},
    {'customer': 'Bob', 'product': 'Jeans', 'amount': 3, 'unit_price': 40.0},
    {'customer': 'Ethan', 'product': 'T-shirt', 'amount': 2, 'unit_price': 15.0},
    {'customer': 'Fiona', 'product': 'Hat', 'amount': 1, 'unit_price': 20.0},
    {'customer': 'George', 'product': 'Jacket', 'amount': 2, 'unit_price': 80.0},
    {'customer': 'Hannah', 'product': 'Sweater', 'amount': 1, 'unit_price': 35.0},
    {'customer': 'Alice', 'product': 'Sneakers', 'amount': 1, 'unit_price': 50.0},
    {'customer': 'Bob', 'product': 'T-shirt', 'amount': 1, 'unit_price': 15.0},
    {'customer': 'Alice', 'product': 'Hat', 'amount': 2, 'unit_price': 20.0},
    {'customer': 'Charlie', 'product': 'Sweater', 'amount': 1, 'unit_price': 35.0},
    {'customer': 'Diana', 'product': 'T-shirt', 'amount': 1, 'unit_price': 15.0},
    {'customer': 'George', 'product': 'Sneakers', 'amount': 1, 'unit_price': 50.0},
    {'customer': 'Hannah', 'product': 'Jacket', 'amount': 1, 'unit_price': 80.0},
    {'customer': 'Alice', 'product': 'Jeans', 'amount': 1, 'unit_price': 40.0},
    {'customer': 'Charlie', 'product': 'T-shirt', 'amount': 2, 'unit_price': 15.0},
    {'customer': 'Ethan', 'product': 'Jacket', 'amount': 1, 'unit_price': 80.0},
    {'customer': 'George', 'product': 'Hat', 'amount': 1, 'unit_price': 20.0},
    {'customer': 'Diana', 'product': 'Jeans', 'amount': 2, 'unit_price': 40.0},
    {'customer': 'Fiona', 'product': 'T-shirt', 'amount': 1, 'unit_price': 15.0},
    {'customer': 'Alice', 'product': 'T-shirt', 'amount': 2, 'unit_price': 15.0},
    {'customer': 'Ethan', 'product': 'Sweater', 'amount': 1, 'unit_price': 35.0},
    {'customer': 'Bob', 'product': 'Sneakers', 'amount': 1, 'unit_price': 50.0},
    {'customer': 'George', 'product': 'Jeans', 'amount': 1, 'unit_price': 40.0},
    {'customer': 'Hannah', 'product': 'Hat', 'amount': 2, 'unit_price': 20.0},
    {'customer': 'Charlie', 'product': 'Jacket', 'amount': 1, 'unit_price': 80.0},
    {'customer': 'Alice', 'product': 'Sweater', 'amount': 1, 'unit_price': 35.0},
    {'customer': 'Fiona', 'product': 'Jacket', 'amount': 1, 'unit_price': 80.0},
    {'customer': 'Bob', 'product': 'Hat', 'amount': 1, 'unit_price': 20.0},
    {'customer': 'Diana', 'product': 'Sweater', 'amount': 2, 'unit_price': 35.0},
    {'customer': 'Charlie', 'product': 'Hat', 'amount': 1, 'unit_price': 20.0},
    {'customer': 'George', 'product': 'T-shirt', 'amount': 1, 'unit_price': 15.0},
    {'customer': 'Hannah', 'product': 'T-shirt', 'amount': 1, 'unit_price': 15.0},
    {'customer': 'Alice', 'product': 'Jacket', 'amount': 1, 'unit_price': 80.0},
    {'customer': 'Charlie', 'product': 'Sneakers', 'amount': 1, 'unit_price': 50.0},
    {'customer': 'Ethan', 'product': 'Hat', 'amount': 1, 'unit_price': 20.0},
    {'customer': 'Fiona', 'product': 'Jeans', 'amount': 1, 'unit_price': 40.0},
    {'customer': 'Bob', 'product': 'Sweater', 'amount': 1, 'unit_price': 35.0},
]


# Question 1: Total sales (amount)
total_units_sold = 0
for sale in sales:
    total_units_sold += sale['amount']

print('*** Total sales ***')
print(f' -Total sales by quantity = {total_units_sold}')

# Question 1: Total sales (revenue)
total_revenue = 0

for sale in sales:
    total_revenue += sale['amount'] * sale['unit_price']

print(f' -Total revenue = ${total_revenue:.2f}\n')

# Question 2: Sales by customer
rev_by_cust = {}

for sale in sales:
    customer = sale['customer']
    revenue = sale['amount'] * sale['unit_price']

    if customer in rev_by_cust:
        rev_by_cust[customer] += revenue
    else:
        rev_by_cust[customer] = revenue

print('*** Sales by customer ***')
for name, rev in rev_by_cust.items():
    print(f'Total revenue from {name} = ${rev:.2f}')
print()

# Question 3: Total units sold by product and most sold item by quantity
items_sold = {}
max_quantity = 0
most_sold_item = None

for sale in sales:
    product = sale['product']
    quantity = sale['amount']

    if product in items_sold:
        items_sold[product] += quantity
    else:
        items_sold[product] = quantity

for item, quantity in items_sold.items():
    if quantity > max_quantity:
        max_quantity = quantity
        most_sold_item = item

print('*** Total units sold by product and most sold item by quantity ***')
for prod, quant in items_sold.items():
    print(f'Product: {prod:<10} Units sold = {quant}')
print(f'\nThe most sold product by quantity is: {most_sold_item}\n')

# Question 4: Count of transactions by customer
transx_count = {}

for sale in sales:
    customer = sale['customer']

    if customer in transx_count:
        transx_count[customer] += 1
    else:
        transx_count[customer] = 1

print('*** Transactions count by customer ***')
for name, count in transx_count.items():
    print(f'The client {name} has made {count} purchases.')
print()

# Question 5: Grouped sales by customer and product
grouped_sales = {}

for sale in sales:
    customer = sale['customer']
    product = sale['product']
    revenue = sale['amount'] * sale['unit_price']

    if customer not in grouped_sales:
        grouped_sales[customer] = {}

    if product not in grouped_sales[customer]:
        grouped_sales[customer][product] = revenue
    else:
        grouped_sales[customer][product] += revenue

print('*** Revenue grouped by customer and product ***')
for clt, products in grouped_sales.items():
    print(f' -> Client: {clt}')
    for prod, rev in products.items():
        print(f'  --> Product: {prod:<10} Revenue: ${rev:.2f}')



