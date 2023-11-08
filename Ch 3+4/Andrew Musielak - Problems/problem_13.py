# Average grade calculator
keepAdding = True
sum = 0
numTest = 0

while keepAdding:
    grade = float(input("Please enter the grade or -1 to stop inputing: "))
    if grade == -1.0:
        break
    while grade < 0:
        grade = float(input("Please enter a valid grade: "))

    sum += grade
    numTest += 1

average = sum/numTest

print(f"The average for {numTest} tests is {average}%.")
