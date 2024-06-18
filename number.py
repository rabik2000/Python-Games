import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please Start with a number that is greater than 0')
        quit()
else:
    print('Please type a number next time')
    quit()
random_number = random.randint(1, top_of_range)
guess = 0

while True:
    guess += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time')
        continue

    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess > random_number:
            print("Your guess is too high")
    else:
            print('Your guess is too low')

print("You got it in " + str(guess) + " guesses!")