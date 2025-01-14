cafeteria_menu = ""
print("Cafeteria Menu: " )
print("1. Pizza" "\n" "2. Sandwich" "\n" "3. Salad" "\n" "4. Soda" "\n" "5. Dessert" "\n" "0. Finish Order")



while True:
    item = input("Enter the item number you want to order: ") #input
    if item == '1':
        cafeteria_menu = cafeteria_menu + "Pizza" + "\n"
    elif item == '2':
        cafeteria_menu = cafeteria_menu + "Sandwich" + "\n"
    elif item == '3':
        cafeteria_menu = cafeteria_menu + "Salad" + "\n"
    elif item == '3':
        cafeteria_menu = cafeteria_menu + "Soda" + "\n"
    elif item == '5':
        cafeteria_menu = cafeteria_menu + "Dessert" + "\n"
    elif item == '0':
        print("Order Complete\n ")
        break
    else:
        print("Invalid item entered")

print("Your Orders: ")
print(cafeteria_menu)

    