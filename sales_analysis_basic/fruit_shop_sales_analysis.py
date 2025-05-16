# Mini-project: Analyzing sales data

# Question 1: Total sales (amount and revenue)
# Question 2: Sales by customer
# Question 3: Most sold item by quantity
# Question 4: Count of transactions by customer

sales = [
    {"customer": "Alice", "item": "apple", "amount": 50, "unit_price": 0.5},
    {"customer": "Bob", "item": "banana", "amount": 30, "unit_price": 0.4},
    {"customer": "Alice", "item": "banana", "amount": 20, "unit_price": 0.4},
    {"customer": "Charlie", "item": "apple", "amount": 40, "unit_price": 0.5},
    {"customer": "Bob", "item": "apple", "amount": 10, "unit_price": 0.5}
]

# 1) Calculate total sales (amount)
total_sales = 0

for sale in sales:
    total_sales += sale["amount"]

print("Total sales amount:", total_sales) # Total sales amount: 15

# 1) Calculate total revenue
total_revenue = 0

for sale in sales:
    revenue = sale["amount"] * sale["unit_price"]
    total_revenue += revenue

print(f'Total revenue: ${total_revenue:.0f}\n')


# 2) Calculate revenue per customer

revenue_by_customer = {}

for sale in sales:
    customer = sale["customer"]
    revenue = sale["amount"] * sale["unit_price"]

    if customer in revenue_by_customer:
        revenue_by_customer[customer] += revenue
    else:
        revenue_by_customer[customer] = revenue

print("Revenue by customer:\n")
for customer, revenue in revenue_by_customer.items():
    print(f'{customer} bought ${revenue:.0f}')

print()

# 3) Most sold item by quantity

items_sold = {}

for sale in sales:
    item = sale["item"]
    amount = sale["amount"]

    if item in items_sold:
        items_sold[item] += amount
    else:
        items_sold[item] = amount

# Find the item with the highest quantity
most_sold_item = None
max_quantity = 0

for item, quantity in items_sold.items():
    if quantity > max_quantity:
        max_quantity = quantity
        most_sold_item = item
print("Most sold item by quantity")
print("Items sold:", items_sold)
print("Most sold item:", most_sold_item, "with", max_quantity, "units")

print()

# 4) How many transactions made each customer

transactions_count = {}

for client in sales:
    customer = client["customer"]

    if customer in transactions_count:
        transactions_count[customer] += 1
    else:
        transactions_count[customer] = 1

print("Transactions per customer:")
for customer, count in transactions_count.items():
    print(f"{customer} has bought {count} times")








