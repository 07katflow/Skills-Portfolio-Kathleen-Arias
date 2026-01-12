bouquets_orders = ["Wedding Bouquets", "Sweetheart Bouquets", "Bridal Bouquets", "Toss Bouquets"]
finished_bouquets = []

while bouquets_orders:
    current_bouquet = bouquets_orders.pop()
    print("I'm working on your " + current_bouquet + " now.")
    finished_bouquets.append(current_bouquet)

    print("\n")
    for bouquet in finished_bouquets:
        print("I made your " + bouquet + ".")

print('\n')

word = input("Enter a word: ")
for letter in word:
    print(letter)