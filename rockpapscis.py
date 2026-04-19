import random

random.seed(100)
rand = random.randint(1, 3)

print("You about to play Rock, Paper, Scissors")
while True:
    print("Choose your choice")
    print("Rock = 1, paper = 2, scissors = 3")
    choice = int(input("Enter your choice habibi: "))

    match choice:
        case 1:
            if rand == 2:
                print("Paper beats rock")
            elif rand == 3:
                print("Rock beats Scissor")
            elif rand == 1:
                print("This is a draw brother")
        case 2:
            if rand == 1:
                print("Paper beats rock")
            elif rand == 3:
                print("Scissor beats Paper")
            elif rand == 2:
                print("This is a draw brother")
        case 3:
            if rand == 1:
                print("Rock beats Scissor")
            elif rand == 2:
                print("Paper beats rock")
            elif rand == 3:
                print("This is a draw brother")
        case _:
            print("Wrong number bro")
            break