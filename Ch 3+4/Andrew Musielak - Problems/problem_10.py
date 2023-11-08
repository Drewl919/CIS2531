# Percent to letter grade converter
grade = float(input("Please enter the grade: "))
while grade < 0:
    grade = float(input("Please enter a valid grade: "))

if grade >= 89.5:
    print("The grade is an A")
elif grade >= 79.5:
    print("The grade is a B")
elif grade >= 69.5:
    print("The grade is a C")
elif grade >= 59.5:
    print("The grade is a D")
else:
    print("The grade is a F")