import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit:  ").lower()
    if user_input == "q":
        break

    if user_input not in options :
        continue

    random_number = random.randint(0, 2)
    computer_choice = options[random_number]
    print("Computer picked", computer_choice + ".")

    if user_input == "rock" and computer_choice == "scissors":
        print("You win!")
        user_wins += 1

    elif user_input == "paper" and computer_choice == "rock":
        print("You win!")
        user_wins += 1

    elif user_input == "scissors" and computer_choice == "paper":
        print("You win!")
        user_wins += 1
        continue

    elif user_input == computer_choice:
        print("Draw! Try Again")
        continue

    else:
        print("You lose!")
        computer_wins += 1


print("Yow won: ", user_wins, "times.")
print("Computer won: ", computer_wins, "times.")
print("Thanks for Playing!")
