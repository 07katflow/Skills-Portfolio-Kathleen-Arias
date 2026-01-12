lang = input("Enter your programming language: ").capitalize()
match lang:
    case 'Python':
        print("Great choice!")
    case 'JavaScript':
        print("Good for web development!")
    case 'Java':
        print("Good for enterprise applications!")
    case _:
        print("That's an interesting language!")

print("\n")

color_of_shirt = input("What is the color of your shirt? ")
if color_of_shirt == 'blue':
    print("Nice! blue shirt")
else:
    print("That's not a blue shirt!")

print("\n")

student_name = input("Enter your name: ")
marks = int(input("What is your marks? "))

if marks <=100 and marks >= 90:
    print("Grade: A")
    message = "Excellent work, " + student_name + "!"
elif marks < 90 and marks >= 80:
    print("Grade: B")
    message = "Good job, " + student_name + "!"
elif marks < 80 and marks >= 70:
    print("Grade: C")
    message = "You passed, " + student_name + "."
elif marks < 70 and marks >= 60:
    print("Grade: D")
    message = "You need to improve, " + student_name + "."
else:
    print("Grade: F")
    message = "You failed, Better luck next time, " + student_name + "."

print("Student Name: " + student_name)
print("Marks: " + str(marks))
print(message)