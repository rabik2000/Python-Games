name = input("Type your name: ")
print("Welcome " + name + " to this adventure!")\

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go left or right? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Do you wanna walk or swim? ").lower()

    if answer == "swim":
        print("You swam and were eaten by an alligator")
    elif answer == "walk":
        print("You walk across the road and lose")

elif answer == "right":
    answer = input("You cross the bridge and met a stranger. Do you talk to them (yes/no)? ").lower()

    if answer == "yes":
        print("You talk to the stranger and give you gold. You WIN!")
    elif answer == "no":
        print("You ignore the stranger and they are offended and you lose.")
    else:
        print("Not a valid answer. You lose")

else:
    print("Not a Valid Option. you Lose!")

print("Thank you for playing this adventure!")