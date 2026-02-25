thing1 = {'code': 'A1', 'name': 'Cola', 'price': 1.50, 'quantity': 10}
thing2 = {'code': 'B2', 'name': 'Chips', 'price': 1.00, 'quantity': 15}
thing3 = {'code': 'C3', 'name': 'Starburst', 'price': 2.75, 'quantity': 20}
thing4 = {'code': 'D4', 'name': 'Water', 'price': 1.25, 'quantity': 12}
thing5 = {'code': 'E5', 'name': 'Skittles', 'price': 3.50, 'quantity': 0} # Out of stock
thing6 = {'code': 'F6', 'name': 'Gummy Bears', 'price': 1.50, 'quantity': 30}

print("Welcome! How can I help you today?")

while True:
    print("\nThe available items are: \n")
    print(f"{thing1['code']}: {thing1['name']} - AED {thing1['price']}")
    print(f"{thing2['code']}: {thing2['name']} - AED {thing2['price']}")
    print(f"{thing3['code']}: {thing3['name']} - AED {thing3['price']}")
    print(f"{thing4['code']}: {thing4['name']} - AED {thing4['price']}")
    print(f"{thing5['code']}: {thing5['name']} - AED {thing5['price']}")
    print(f"{thing6['code']}: {thing6['name']} - AED {thing6['price']}")
    print("\n")
    
    selected_item = input("Select an item code to purchase (or type 'n' to quit): ").upper()
    
    if(selected_item == 'A1') and (thing1['quantity'] > 0):
        payment = float(input("How much money do you want to pay for " + thing1['name'] + "?: AED "))
        if(payment >= thing1['price']) or (payment > thing1['price']):
            print("Dispensing " + thing1['name'])
            balance = payment - thing1['price']
            if balance > 0:
                print("Returning change: AED " + str(balance))
            thing1['quantity'] -= 1
        else:
            print("Insufficient payment. Transaction cancelled.")

    elif(selected_item == 'B2') and (thing2['quantity'] > 0):
        payment = float(input("How much money do you want to pay for " + thing2['name'] + "?: AED "))
        if(payment >= thing2['price']) or (payment > thing2['price']):
            print("Dispensing " + thing2['name'])
            balance = payment - thing2['price']
            if balance > 0:
                print("Returning change: AED " + str(balance))
            thing2['quantity'] -= 1
        else:
            print("Insufficient payment. Transaction cancelled.")

    elif(selected_item == 'C3') and (thing3['quantity'] > 0):
        payment = float(input("How much money do you want to pay for " + thing3['name'] + "?: AED "))
        if(payment >= thing3['price']) or (payment > thing3['price']):
            print("Dispensing " + thing3['name'])
            balance = payment - thing3['price']
            if balance > 0:
                print("Returning change: AED " + str(balance))
            thing3['quantity'] -= 1
        else:
            print("Insufficient payment. Transaction cancelled.")

    elif(selected_item == 'D4') and (thing4['quantity'] > 0):
        payment = float(input("How much money do you want to pay for " + thing4['name'] + "?: AED "))
        if(payment >= thing4['price']) or (payment > thing4['price']):
            print("Dispensing " + thing4['name'])
            balance = payment - thing4['price']
            if balance > 0:
                print("Returning change: AED " + str(balance))
            thing4['quantity'] -= 1
        else:
            print("Insufficient payment. Transaction cancelled.")
        
    elif(selected_item == 'E5') and (thing5['quantity'] == 0):
        print("Sorry, this item is out of stock.")

    elif(selected_item == 'F6') and (thing6['quantity'] > 0):
        payment = float(input("How much money do you want to pay for " + thing6['name'] + "?: AED "))
        if(payment >= thing6['price']) or (payment > thing6['price']):
            print("Dispensing " + thing6['name'])
            balance = payment - thing6['price']
            if balance > 0:
                print("Returning change: AED " + str(balance))
            thing6['quantity'] -= 1
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