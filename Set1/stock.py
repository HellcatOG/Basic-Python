num_items = int(input("Enter the number of items: "))

items = []
quantity = []

# Loop to input 
for i in range(num_items):
    item_name = input(f"Enter item {i+1} name: ")
    quantity_list = int(input(f"Enter item {i+1} quantity: "))  
    
    items.append(item_name)
    quantity.append(quantity_list)

# Low-stock alert 
print("\nLow-stock alert! The following items have less than 5 units:")
for i in range(num_items):
    if quantity[i] < 5:
        print(f" {items[i]}: {quantity[i]} units")

item_to_update = input("Enter the item to update: ")
if item_to_update in items:
    index = index(item_to_update)
    
    
 \     print(f"")
    
