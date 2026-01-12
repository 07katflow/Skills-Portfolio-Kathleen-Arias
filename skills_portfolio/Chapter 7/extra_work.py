def cities(city, country):
    msg = city + " is in " + country
    print(msg)

cities("Tokyo", "Japan")
cities("Manila", "Philippines")
cities("Jakarta", "Indonesia")

print("\n")

def new():
    def hello():
        print("Hello Kat")
        print("How are you?")
        print("I am doing great!")
        
    def main():
        hello()
    print("This is the main function")
    main()
new()

print('\n')

def area(x, y):
    return (x * y)

w = int(input("Enter width: "))
h = int(input("Enter height: "))
print("Area is:", area(w, h))