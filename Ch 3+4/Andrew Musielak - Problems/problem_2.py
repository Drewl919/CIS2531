
toDisplay = int(input("How many Fibonacci numbers would you like displayed? "))
while toDisplay < 0:
    toDisplay = int(input("Please enter a value greater than 0: "))

count = 0
first = 1
second = 1

while count < toDisplay:
    print(first, end = " ")
    newN = first + second
    first = second
    second = newN
    count += 1
