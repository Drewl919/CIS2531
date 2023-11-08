# Prints the sum of all digits added together
num = int(input("Please enter a number: "))

toDisplay = num
sum = 0

while num != 0:
    sum += int(num % 10)
    num = int(num / 10)

print(f"The sum of the digits for {toDisplay} is equal to {sum}")