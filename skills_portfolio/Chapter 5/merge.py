student1 = {
    'name': 'alpha',
    'marks': {'Codelab1 - 78', 'Codelab2 - 82'},
}
year = {
    'Year': 2022
}
student1.update(year)
print(student1)

print('\n')

letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
    print(f'Letter: {l}')
    print(f'Number: {n}')