invalid = 100
user_input = int(input("please enter your age: "))
if user_input < 18:
    print("you are not eligible to vote")
elif user_input > invalid:
    print("RIP")
elif user_input >= 18:
    print("you are  eligible to vote")