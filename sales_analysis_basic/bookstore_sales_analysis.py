# Mini-project: Analyzing sales data

# Question 1: Total sales (amount and revenue)
# Question 2: Sales by customer
# Question 3: Most sold item by quantity
# Question 4: Count of transactions by customer

sales = [
    {"customer": "Liam", "product": "1984", "amount": 2, "unit_price": 15.0},
    {"customer": "Olivia", "product": "The Hobbit", "amount": 1, "unit_price": 18.5},
    {"customer": "Emma", "product": "The Catcher in the Rye", "amount": 3, "unit_price": 12.0},
    {"customer": "Noah", "product": "To Kill a Mockingbird", "amount": 2, "unit_price": 16.0},
    {"customer": "Liam", "product": "The Great Gatsby", "amount": 1, "unit_price": 14.0},
    {"customer": "Ava", "product": "1984", "amount": 2, "unit_price": 15.0},
    {"customer": "Isabella", "product": "The Hobbit", "amount": 2, "unit_price": 18.5},
    {"customer": "Sophia", "product": "1984", "amount": 1, "unit_price": 15.0},
    {"customer": "Mason", "product": "To Kill a Mockingbird", "amount": 3, "unit_price": 16.0},
    {"customer": "Liam", "product": "The Hobbit", "amount": 1, "unit_price": 18.5},
    {"customer": "Olivia", "product": "The Catcher in the Rye", "amount": 2, "unit_price": 12.0},
    {"customer": "Ava", "product": "The Great Gatsby", "amount": 1, "unit_price": 14.0},
    {"customer": "Noah", "product": "The Hobbit", "amount": 2, "unit_price": 18.5},
    {"customer": "Emma", "product": "1984", "amount": 3, "unit_price": 15.0},
    {"customer": "Sophia", "product": "The Great Gatsby", "amount": 2, "unit_price": 14.0},
    {"customer": "Isabella", "product": "The Catcher in the Rye", "amount": 1, "unit_price": 12.0},
    {"customer": "Mason", "product": "1984", "amount": 2, "unit_price": 15.0},
    {"customer": "Ava", "product": "To Kill a Mockingbird", "amount": 1, "unit_price": 16.0},
    {"customer": "Liam", "product": "1984", "amount": 1, "unit_price": 15.0},
    {"customer": "Olivia", "product": "To Kill a Mockingbird", "amount": 1, "unit_price": 16.0},
    {"customer": "Emma", "product": "The Hobbit", "amount": 2, "unit_price": 18.5},
    {"customer": "Noah", "product": "The Great Gatsby", "amount": 2, "unit_price": 14.0},
    {"customer": "Sophia", "product": "The Catcher in the Rye", "amount": 2, "unit_price": 12.0},
    {"customer": "Isabella", "product": "To Kill a Mockingbird", "amount": 3, "unit_price": 16.0},
    {"customer": "Mason", "product": "The Hobbit", "amount": 1, "unit_price": 18.5},
    {"customer": "Liam", "product": "To Kill a Mockingbird", "amount": 2, "unit_price": 16.0},
    {"customer": "Ava", "product": "The Catcher in the Rye", "amount": 1, "unit_price": 12.0},
    {"customer": "Noah", "product": "1984", "amount": 1, "unit_price": 15.0},
    {"customer": "Emma", "product": "The Great Gatsby", "amount": 2, "unit_price": 14.0},
    {"customer": "Mason", "product": "The Catcher in the Rye", "amount": 2, "unit_price": 12.0},
    {"customer": "Olivia", "product": "1984", "amount": 2, "unit_price": 15.0},
]


# Question 1: Total sales (amount)
sold_unts = 0

for sale in sales:
    sold_unts += sale['amount']
print('*** Total sales ***')
print(f' -Total sales by quantity = {sold_unts}')

# Question 1: Total sales (revenue)

revenue = 0

for sale in sales:
    revenue += sale['unit_price'] * sale['amount']

print(f' -Total revenue = ${revenue:.2f}\n')

# Question 2: Sales by customer

sales_per_cust = {}

for sale in sales:
    client = sale['customer']
    rev_per_cust = sale['unit_price'] * sale['amount']

    if client not in sales_per_cust:
        sales_per_cust[client] = rev_per_cust
    else:
        sales_per_cust[client] += rev_per_cust

print('*** Sales per customer ***')
for name, rev in sales_per_cust.items():
    print(f' -Client: {name}, Sales: ${rev:.2f}')

print()

# Question 3: Most sold item by quantity

best_product = {}
max_quantity = 0
most_sold = None

for sale in sales:
    product = sale['product']
    units = sale['amount']

    if product not in best_product:
        best_product[product] = units
    else:
        best_product[product] += units

for prod, unt in best_product.items():
    if unt > max_quantity:
        max_quantity = unt
        most_sold = prod

print('*** Most sold item by quantity ***')
print(f' The book {most_sold} with {max_quantity} units.\n')


# Question 4: Count of transactions by customer

count_of_transx = {}

for sale in sales:
    name = sale['customer']

    if name not in count_of_transx:
        count_of_transx[name] = 1
    else:
        count_of_transx[name] += 1

print('*** Transactions count by customer ***')
for name, count in count_of_transx.items():
    print(f' The client {name} has made {count} purchases')













