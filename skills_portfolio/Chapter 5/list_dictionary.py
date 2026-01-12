student1 = {'name': 'alpha', 'id': 5, 'course': 'BSC CYBERSECURITY'}
student2 = {'name': 'beta', 'id': 6, 'course': 'BSC CREATIVE COMPUTING'}
student3 = {'name': 'gamma', 'id': 7, 'course': 'BSC DATA SCIENCE'}
student4 = {'name': 'delta', 'id': 8, 'course': 'BSC SOFTWARE ENGINEERING'}

student_list = [student1, student2, student3, student4]
for std in student_list:
    print(std)

student = {
    'name': 'alpha',
    'marks': ['Codelab1 - 78', 'Codelab2 - 82'],
}

print(f"The student name is: {student['name']} scored the following marks:")
for mark in student['marks']:
    print(f"\t + {mark}")