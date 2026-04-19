import random

random.seed(100)
rand = random.randint(1, 100)

while True:
    num = int(input("Enter a number between 1 and 100: "))

    if num < rand:
        print("Too low")
    elif num > rand:
        print("Too high")
    else:
        print("Correct")
        break