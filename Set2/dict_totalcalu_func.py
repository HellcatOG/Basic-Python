def calculate_total(order):
    total = 0
    for item in order:
        if item['quantity'] > 0:  # Ensure only valid items are included
            total += item['quantity'] * item['price']
    return total

# Example Input
order = [
    {'item_name': 'Laptop', 'quantity': 1, 'price': 800},
    {'item_name': 'Mouse', 'quantity': 2, 'price': 25},
    {'item_name': 'Keyboard', 'quantity': 0, 'price': 40},
    {'item_name': 'Monitor', 'quantity': 1, 'price': 300}
]

# Calculate Total
result = calculate_total(order)

# Output
print(result)
