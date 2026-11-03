print("Welcome to treasure island. Your mission is to find the treasure")

choice1 = input('You\'re at a crossroad, where do you want to go? "left" or "right.').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to the lake, there is an island in the middle  of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross.').lower()

    if choice2 == "wait":
        choice3 = input("You arrived at the island unharmed. There is a house with 3 doors. one red, one yellow and one blue. Which color did you choose?").lower()
        if choice3 == "red":
            print("Game over")
        elif choice3 == "yellow":
            print("You found the treasure. You win!")
        elif choice3 == "blue":
            print("Game over")
        else:
            print("Door does not exist. game over")
    else:
        print("You got attacked")

else:
    print("Game over")