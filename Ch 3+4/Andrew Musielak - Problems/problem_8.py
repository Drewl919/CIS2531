# Prints all positive prime numbers up to 100
for possPrime in range(2, 100):
    isPrime = True
    for divisor in range(2, possPrime):
        if possPrime % divisor == 0:
            isPrime = False
            break
    if isPrime:
        print(possPrime, end = " ")