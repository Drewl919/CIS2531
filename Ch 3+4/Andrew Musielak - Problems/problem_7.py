# Demonstrating displaying with loops
rows = int(input("How many rows would you like? "))
while rows < 1:
    rows = int(input("Please enter a value greater than 0: "))

count = 0
curRow = 1

while curRow < rows+1:
    if count != curRow:
        print("*", end="")
        count += 1
    else:
        curRow += 1
        count = 0
        print()