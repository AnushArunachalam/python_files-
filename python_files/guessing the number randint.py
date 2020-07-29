import random
chance = 0
while chance < 7:
    user_input = int(input("please enter number between 1 to 20:- "))
    random_number = random.randint(1, 21)
    if user_input == random_number:
        print("you have WON ")
        break
    elif user_input != random_number:
        chance += 1
        print("TRY AGAIN ! ")
    if chance == 7:
        print("sorry you LOSE ! ")