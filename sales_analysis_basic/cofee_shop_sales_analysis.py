# Mini-project: Analyzing sales data

# Question 1: Total sales (amount and revenue)
# Question 2: Sales by customer
# Question 3: Most sold item by quantity
# Question 4: Count of transactions by customer

sales = [
    {"customer": "Diana", "product": "latte", "amount": 3, "unit_price": 4.5},
    {"customer": "Ethan", "product": "espresso", "amount": 2, "unit_price": 3.0},
    {"customer": "Fiona", "product": "cappuccino", "amount": 1, "unit_price": 4.0},
    {"customer": "Diana", "product": "espresso", "amount": 1, "unit_price": 3.0},
    {"customer": "George", "product": "latte", "amount": 2, "unit_price": 4.5},
    {"customer": "Fiona", "product": "latte", "amount": 2, "unit_price": 4.5},
    {"customer": "Ethan", "product": "cappuccino", "amount": 2, "unit_price": 4.0},
    {"customer": "Diana", "product": "latte", "amount": 1, "unit_price": 4.5},
    {"customer": "Hannah", "product": "americano", "amount": 2, "unit_price": 3.5},
    {"customer": "George", "product": "mocha", "amount": 1, "unit_price": 5.0},
    {"customer": "Diana", "product": "americano", "amount": 1, "unit_price": 3.5},
    {"customer": "Fiona", "product": "mocha", "amount": 2, "unit_price": 5.0},
    {"customer": "Ethan", "product": "latte", "amount": 1, "unit_price": 4.5},
    {"customer": "George", "product": "espresso", "amount": 3, "unit_price": 3.0},
    {"customer": "Hannah", "product": "latte", "amount": 2, "unit_price": 4.5},
    {"customer": "Diana", "product": "cappuccino", "amount": 2, "unit_price": 4.0},
    {"customer": "Ethan", "product": "mocha", "amount": 1, "unit_price": 5.0},
    {"customer": "George", "product": "americano", "amount": 2, "unit_price": 3.5},
    {"customer": "Hannah", "product": "cappuccino", "amount": 1, "unit_price": 4.0},
    {"customer": "Fiona", "product": "americano", "amount": 1, "unit_price": 3.5}
]


# Question 1: Total sales (amount)

sold_units = 0

for sale in sales:
    sold_units += sale['amount']

print(f'Total units sold: {sold_units}\n')

# Total sales (revenue)

total_revenue = 0

for sale in sales:
    total_revenue += sale['amount'] * sale['unit_price']

print(f'Total revenue: ${total_revenue:.2f}\n')


# Question 2: Sales by customer

sales_by_customer = {}

for sale in sales:
    customer = sale['customer']
    revenue =  sale['amount'] * sale['unit_price']


    sales_by_customer[customer] = sales_by_customer.get(customer, 0) + revenue

print('Sales by customer:')
for customer, revenue in sales_by_customer.items():
    print(f'-Client name: {customer} -> Total revenue: ${revenue:.2f}')

print()
# Question 3: Most sold item by quantity

products_sold = {}

for sale in sales:
    item = sale['product']
    quantity = sale['amount']

    if item in products_sold:
        products_sold[item] += quantity
    else:
        products_sold[item] = quantity

# Find the item with the highest quantity
max_quantity = 0
most_sold_item = None

for item, quantity in products_sold.items():
    if quantity > max_quantity:
        max_quantity = quantity
        most_sold_item = item

print('Most sold item by quantity:')
print(f'Items sold: {list(products_sold.keys())}')
print(f'The most sold product by quantity is: {most_sold_item}, with {max_quantity} units.\n')

# Question 4: Count of transactions by customer

trx_count = {}
count = 0
for client in sales:
    customer = client['customer']

    if customer in trx_count:
        trx_count[customer] += 1
    else:
        trx_count[customer] = 1

print("Transactions per customer:")
for customer, amount in trx_count.items():
    print(f'-Client name: {customer} has bought {amount} times')


















