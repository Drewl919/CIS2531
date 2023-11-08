# Adds up all numbers from 1 to n
maxValue = int(input("Please enter a number greater than 0: "))
while maxValue < 0:
    maxValue = int(input("Please enter a number greater than 0: "))

count = 1

sum = 0

while count < maxValue + 1:
    sum += count
    count += 1

print(sum)