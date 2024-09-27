# Conditional Statements and while loops
# Author: Titus Sim
# Date: 2024-09-27
# Version 1
# TODO: Create a program that asks a program that asks a user a questions 
# and returns a response based on the answer of the user. 


# Main loop. Keeps running until a condition is met
keep_going = ""
while keep_going == "":

    like_coffee = input("Do you like drinking coffee?").lower()

    if like_coffee == "yes" or like_coffee == "y":
        print("I like coffee as well!!")
    elif like_coffee == "no" or like_coffee == "n":
        print("That's alright, coffee is not for everyone.")

        like_tea = input("Would you like tea instead?").lower()
        if like_coffee == "no" or like_coffee == "n":
            print(like_tea)
        if like_tea == "yes" or like_tea == "y":
            print("That's great! Tea is very nice")
        elif like_tea == "no" or like_coffee == "n":
            print("aww shucks, you are missing out man!")


    else:
        print("I dont understand")

    keep_going = input("Press <enter> to continue or any other key to quit")




