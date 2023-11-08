# Demonstrates displaying using loops and user input to create a board
rows = int(input("How many rows would you like? "))
while rows < 1:
    rows = int(input("Please enter a value greater than 0: "))

spotRow = 0
curRow = 1

value = 1

while curRow < rows+1:
    while spotRow < rows:
        if value % 2 == 0:
            print("o", end=" ")
        else:
            print("x", end=" ")
        spotRow += 1
        value += 1
    curRow += 1
    spotRow = 0
    print()