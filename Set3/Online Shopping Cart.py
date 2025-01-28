shopping_cart = []

def add_to_cart(product_name, quantity, price):
    item = {
        'product': product_name,
        'quantity': quantity,
        'price': price
    }
    shopping_cart.append(item)

def calculate_total():
    subtotal = sum(item['price'] * item['quantity'] for item in shopping_cart)
    total_with_tax = subtotal * 1.05  
    return total_with_tax

def main():
    add_to_cart('Laptop', 1, 1000)
    add_to_cart('Mouse', 2, 25)


    total = calculate_total()
    print(f"Cart Items: {shopping_cart}")
    print(f"Total with Tax: {total:.2f}")

main()
