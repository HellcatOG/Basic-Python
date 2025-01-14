price= []
while True:
    amount = float(input("Enter the price of an item (enter 0 to finish): "))
    if amount == 0:
        break
    
    price.append(amount)
    total = sum(price)

    
if total > 100:
     discount = (10/100) * total
     final_price = total - discount
     print(f"Total price: {total}")
     print(f"Discount applied! New total: {final_price}")
     
else:
    print(f"Total price: {total}")5
    
    