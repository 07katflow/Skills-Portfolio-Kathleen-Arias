item1 = {'code': 'A1', 'name': 'Cola', 'price': 1.50, 'quantity': 10}
item2 = {'code': 'B2', 'name': 'Chips', 'price': 1.00, 'quantity': 15}
item3 = {'code': 'C3', 'name': 'Starburst', 'price': 2.75, 'quantity': 20}
item4 = {'code': 'D4', 'name': 'Water', 'price': 1.25, 'quantity': 12}
item5 = {'code': 'E5', 'name': 'Skittles', 'price': 3.50, 'quantity': 0} # Out of stock
item6 = {'code': 'F6', 'name': 'Gummy Bears', 'price': 1.50, 'quantity': 30}

print("Welcome! How can I help you today?")

while True:
    print("\nThe available items are: \n")
    print(f"{item1['code']}: {item1['name']} - AED {item1['price']}")
    print(f"{item2['code']}: {item2['name']} - AED {item2['price']}")
    print(f"{item3['code']}: {item3['name']} - AED {item3['price']}")
    print(f"{item4['code']}: {item4['name']} - AED {item4['price']}")
    print(f"{item5['code']}: {item5['name']} - AED {item5['price']}")
    print(f"{item6['code']}: {item6['name']} - AED {item6['price']}")
    print("\n")
    
    selected_item = input("Select an item code to purchase (or type 'n' to quit): ").upper()
    
    if(selected_item == 'A1') and (item1['quantity'] > 0):
        payment = float(input("How much money do you want to pay for " + item1['name'] + "?: AED "))
        if(payment >= item1['price']) or (payment > item1['price']):
            print("Dispensing " + item1['name'])
            balance = payment - item1['price']
            if balance > 0:
                print("Returning change: AED " + str(balance))
            item1['quantity'] -= 1
        else:
            print("Insufficient payment. Transaction cancelled.")

    elif(selected_item == 'B2') and (item2['quantity'] > 0):
        payment = float(input("How much money do you want to pay for " + item2['name'] + "?: AED "))
        if(payment >= item2['price']) or (payment > item2['price']):
            print("Dispensing " + item2['name'])
            balance = payment - item2['price']
            if balance > 0:
                print("Returning change: AED " + str(balance))
            item2['quantity'] -= 1
        else:
            print("Insufficient payment. Transaction cancelled.")

    elif(selected_item == 'C3') and (item3['quantity'] > 0):
        payment = float(input("How much money do you want to pay for " + item3['name'] + "?: AED "))
        if(payment >= item3['price']) or (payment > item3['price']):
            print("Dispensing " + item3['name'])
            balance = payment - item3['price']
            if balance > 0:
                print("Returning change: AED " + str(balance))
            item3['quantity'] -= 1
        else:
            print("Insufficient payment. Transaction cancelled.")

    elif(selected_item == 'D4') and (item4['quantity'] > 0):
        payment = float(input("How much money do you want to pay for " + item4['name'] + "?: AED "))
        if(payment >= item4['price']) or (payment > item4['price']):
            print("Dispensing " + item4['name'])
            balance = payment - item4['price']
            if balance > 0:
                print("Returning change: AED " + str(balance))
            item4['quantity'] -= 1
        else:
            print("Insufficient payment. Transaction cancelled.")
        
    elif(selected_item == 'E5') and (item5['quantity'] == 0):
        print("Sorry, this item is out of stock.")

    elif(selected_item == 'F6') and (item6['quantity'] > 0):
        payment = float(input("How much money do you want to pay for " + item6['name'] + "?: AED "))
        if(payment >= item6['price']) or (payment > item6['price']):
            print("Dispensing " + item6['name'])
            balance = payment - item6['price']
            if balance > 0:
                print("Returning change: AED " + str(balance))
            item6['quantity'] -= 1
        else:
            print("Insufficient payment. Transaction cancelled.")
    else:
        print("Invalid selection. Please try again.")
        continue

    extra = input("Would you like to buy another item? (y/n): ").lower()
    if extra != 'y':
        if selected_item == 'n':
            print("Thank you for using the vending machine. Goodbye!")
        break