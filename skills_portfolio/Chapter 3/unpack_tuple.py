years = (1987, 1985, 1981, 2000)
years1, years2, years3, years4 = years
print("The value of year 1 is:", years1)
print("The value of year 2 is:", years2)
print("The value of year 3 is:", years3)
print("The value of year 4 is:", years4)

y1,*y = years
print("The value of year 1 is:", y1)
print("The grouped values are:", *y)