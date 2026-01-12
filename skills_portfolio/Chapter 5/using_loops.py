student = {'name': 'alpha', 'id': 5, 'course': 'BSC CYBERSECURITY'}
print('Display key-value pairs')
for key, value in student.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
print('\nDisplay only keys')
for key in student.keys():
    print(key)

print('\nDisplay only values')
for value in student.values():
    print(value)