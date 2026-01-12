i = 1
n = 5
while i <= n:
    print(i)
    i = i + 1

print('\n')

total = 0
num = int(input("Enter a number: "))
while num != 0:
    total += num
    num = int(input("Enter a number: "))
print("Total:", total)