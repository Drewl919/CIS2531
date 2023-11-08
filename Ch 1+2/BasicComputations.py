##CIS 2531 - Chapter 2
##Assignment 1 - Basic Computations
##Name: Andrew Musielak
##Date: 6/21/2021

#CHANGE = int(input('Enter the amount of change to convert: '))

CHANGE = 0

#takes input from user
QUARTERS = float(input('Enter number of quarters: '))
DIMES = float(input('Enter number of dimes: '))
NICKELS = float(input('Enter number of nickels: '))
PENNIES = float(input('Enter number of pennies: '))

twenties = 0
tens = 0
fives = 0
ones = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

q = 0.0
d = 0.0
n = 0.0
p = 0.0

#convert the change to the respective side of the decimal place
while QUARTERS > 0:
    q += 0.25
    QUARTERS -= 1
while DIMES > 0:
    d += 0.1
    DIMES -= 1
while NICKELS > 0:
    n += 0.05
    NICKELS -= 1
while PENNIES > 0:
    p += 0.01
    PENNIES -= 1

CHANGE = round(q+d+n+p, 2)
# print("Change: ", CHANGE)

print()
print(f"Number of coins for ${CHANGE} in change is: ")

#checks to see of change equals 0 and continues to run until it does
while CHANGE > 0.01:
    if CHANGE >= 20.0:
        twenties += 1
        CHANGE -= 20.0
        print("added twenty")
        print(CHANGE)
    elif CHANGE > 10.0:
        tens += 1
        CHANGE -= 10.0
        # print("added ten")
        # print(CHANGE)
    elif CHANGE > 5.0:
        fives += 1
        CHANGE -= 5.0
        # print("added five")
        # print(CHANGE)
    elif CHANGE > 1.0:
        ones += 1
        CHANGE -= 1.0
        # print("added one")
        # print(CHANGE)
    if CHANGE >= .25:
        quarters += 1
        CHANGE -= .25
        # print("added quarter")
        # print(CHANGE)
    elif CHANGE >= .10:
        dimes += 1
        CHANGE -= .10
        # print("added dime")
        # print(CHANGE)
    elif CHANGE >= .05:
        nickels += 1
        CHANGE -= .05
        # print("added nickel")
        # print(CHANGE)
    elif CHANGE >= .01:
        pennies += 1
        CHANGE -= .01
        # print("added penny")
        # print(CHANGE)

print(f"Twenties: {twenties}")
print(f"Tens: {tens}")
print(f"Fives: {fives}")
print(f"Ones: {ones}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")