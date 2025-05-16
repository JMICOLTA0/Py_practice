# Mini-project: Analyzing sales data

# Question 1: Total sales (amount and revenue)
# Question 2: Sales by customer
# Question 3: Most sold product by quantity
# Question 4: Count of transactions by customer

sales = [
    {"customer": "Isabel", "product": "wireless mouse", "amount": 2, "unit_price": 15.0},
    {"customer": "Jack", "product": "mechanical keyboard", "amount": 1, "unit_price": 60.0},
    {"customer": "Karen", "product": "USB-C cable", "amount": 3, "unit_price": 8.0},
    {"customer": "Luis", "product": "HDMI cable", "amount": 2, "unit_price": 12.0},
    {"customer": "Maria", "product": "laptop stand", "amount": 1, "unit_price": 25.0},
    {"customer": "Noah", "product": "wireless headphones", "amount": 1, "unit_price": 80.0},
    {"customer": "Olivia", "product": "USB drive 64GB", "amount": 2, "unit_price": 20.0},
    {"customer": "Paul", "product": "external hard drive", "amount": 1, "unit_price": 100.0},
    {"customer": "Quinn", "product": "USB-C cable", "amount": 4, "unit_price": 8.0},
    {"customer": "Rita", "product": "wireless mouse", "amount": 1, "unit_price": 15.0},
    {"customer": "Sam", "product": "mechanical keyboard", "amount": 2, "unit_price": 60.0},
    {"customer": "Tina", "product": "USB-C hub", "amount": 1, "unit_price": 35.0},
    {"customer": "Ursula", "product": "laptop stand", "amount": 2, "unit_price": 25.0},
    {"customer": "Victor", "product": "webcam", "amount": 1, "unit_price": 50.0},
    {"customer": "Wendy", "product": "wireless headphones", "amount": 1, "unit_price": 80.0},
    {"customer": "Xander", "product": "USB drive 64GB", "amount": 3, "unit_price": 20.0},
    {"customer": "Yasmin", "product": "HDMI cable", "amount": 1, "unit_price": 12.0},
    {"customer": "Zane", "product": "wireless mouse", "amount": 2, "unit_price": 15.0},
    {"customer": "Isabel", "product": "webcam", "amount": 1, "unit_price": 50.0},
    {"customer": "Jack", "product": "external hard drive", "amount": 1, "unit_price": 100.0},
    {"customer": "Karen", "product": "USB-C hub", "amount": 2, "unit_price": 35.0},
    {"customer": "Luis", "product": "USB-C cable", "amount": 3, "unit_price": 8.0},
    {"customer": "Maria", "product": "wireless mouse", "amount": 1, "unit_price": 15.0},
    {"customer": "Noah", "product": "USB-C cable", "amount": 2, "unit_price": 8.0},
    {"customer": "Olivia", "product": "mechanical keyboard", "amount": 1, "unit_price": 60.0},
    {"customer": "Paul", "product": "webcam", "amount": 1, "unit_price": 50.0},
    {"customer": "Quinn", "product": "laptop stand", "amount": 1, "unit_price": 25.0},
    {"customer": "Rita", "product": "HDMI cable", "amount": 2, "unit_price": 12.0},
    {"customer": "Sam", "product": "wireless headphones", "amount": 1, "unit_price": 80.0},
    {"customer": "Tina", "product": "USB drive 64GB", "amount": 2, "unit_price": 20.0}
]

# Q1) Total sales (amount)
print(f'Total sales:')
quantity = 0
for sale in sales:
    quantity += sale['amount']

print(f' -> Total units sold = {quantity}')

# Q1) Total sales (revenue)

revenue = 0

for sale in sales:
    revenue += sale['amount'] * sale['unit_price']

print(f' -> Total revenue = ${revenue:.2f}\n')

# Q2) Sales by customer
print('Sales by customer:')

sales_by_cust ={}

for sale in sales:
    customer = sale['customer']
    revenue = sale['amount'] * sale['unit_price']

    if customer not in sales_by_cust:
        sales_by_cust[customer] = revenue
    else:
        sales_by_cust[customer] += revenue

for client, rev in sales_by_cust.items():
    print(f' -> Revenue from {client} = ${rev:.2f}')

print()

# Q3) Most sold product by quantity:
print('Most sold product by quantity:')

most_sold_prod = {}
max_quant = 0
most_sold = None

for sale in sales:
    product = sale['product']
    quant = sale['amount']

    if product in most_sold_prod:
        most_sold_prod[product] += quant
    else:
        most_sold_prod[product] = quant

for prod, quantity in most_sold_prod.items():
    if quantity > max_quant:
        max_quant = quantity
        most_sold = prod

print(f'Products sold: {list(most_sold_prod.keys())}')
print(f'The most sold product by quantity is: {most_sold} with {max_quant} units.\n')

# Q4) Count of transactions by customer
print('Transaction number by customer:')

tranx_count = {}
count = 0

for sale in sales:
    name = sale['customer']

    if name in tranx_count:
        tranx_count[name] += 1
    else:
        tranx_count[name] = 1

for name, count in tranx_count.items():
    print(f' -> Client {name} has bought {count} times.')










