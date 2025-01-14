#input

priceOne = float(input("Enter the price of item One: "))
quantityOne = float(input("Enter the Quantity of item One: "))
priceTwo = float(input("Enter the price of item Two: "))
quantityTwo = float(input("Enter the Quantity of item two"))

#Calculation

subtotalOne = (priceOne*quantityOne);
subtotalTwo = (priceTwo*quantityTwo);
totalPrice = (subtotalOne + subtotalTwo);
discount = (totalPrice/100)*10;
finalAmount = totalPrice-discount;

#Output

print(f"The Subtotal for first item is: {subtotalOne:.2f}")
print(f"The Subtotal for second item is: {subtotalTwo:.2f}")
print(f"The Total Price is: {totalPrice:.2f}")
print(f"The Discount is: {discount:.2f}")
print(f"The Discounted Price is: {finalAmount:.2f}")