# Short multiplication quiz
import random

numCorrect = 0

while numCorrect < 3:
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    aws = num1 * num2
    guess = int(input(f"What is {num1} multiplied by {num2}? "))
    if guess == aws:
        print("You got it right!")
        numCorrect += 1
    else:
        print(f"You did not get the right answer, the answer was {aws}")
        numCorrect = 0

print("You got 3 correct answers in a row!")


