num1 = ["777", "888", "999", "000", "111"]
num1.reverse()
print(num1)

print("\n")

years1 = (1987, 1985, 1981, 2000)
years2 = (1999, 2001, 2003, 2005)
print("Before swapping:")
print("Years1 tuple is:", years1)
print("Years2 tuple is:", years2)
print("\n")
years1, years2 = years2, years1
print("After swapping:")
print("Years1 tuple is:", years1)
print("Years2 tuple is:", years2)

print("\n")

fruits = ["Mango", "Apple", "Banana", "Grapes"]
print(fruits[0])
print(fruits[-1])

print("\n")

list1 = [10, 20, 30, 40, 50]
list2 = [60, 70, 80, 90, 100]
combined_list = list1 + list2
total = sum(combined_list)
print(combined_list)
print(total)

print("\n")

fruits = ["Mango", "Apple", "Banana", "Grapes", "Orange"]
for fruit in fruits:
    print(fruit.upper())

print("\n")

my_list = [5, 10, 15, 20, 25]
my_tuple = tuple(my_list)
print(my_tuple)

my_tuple = (30, 40, 50, 60, 70)
my_list = list(my_tuple)
print(my_list)