# Print out all odd numbers from 1 to n
value = int(input("Please enter a odd number: "))

while value % 2 == 0 or value < 1:
    value = int(input("Please enter a odd number: "))

for i in range (1, value+2, 2):
    print(i, end =" ")