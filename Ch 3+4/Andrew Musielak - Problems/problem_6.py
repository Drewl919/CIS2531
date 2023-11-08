# Demonstrating displaying with loops
count = 0
row = 1

while row < 6:
    if count != row:
        print("*", end="")
        count += 1
    else:
        row += 1
        count = 0
        print()