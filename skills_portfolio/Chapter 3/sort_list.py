pastries = ["croissant", "danish", "eclair", "strudel"]
pastries.sort()
print(pastries)
pastries.sort(reverse=True)
print(pastries)

pastries = ["croissant", "danish", "eclair", "strudel"]
sorted(pastries)
sorted(pastries, reverse=True)
print("\n----------------------------------\n")
pastries = ["croissant", "danish", "eclair", "strudel"]
print("Here is the original list:")
print(pastries)

print("\nHere is the sorted list in alphabetical order:")
print(sorted(pastries))

print("\nHere is the sorted list in reverse alphabetical order:")
print(sorted(pastries, reverse=True))

print("\nHere is the original list again:")
print(pastries)