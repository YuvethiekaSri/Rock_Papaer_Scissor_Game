# This files has the code of playing with computer.
# It first asks for the choice of the players and then for the computer chooses the random choice from the list.
# Based on the choices, Winner is displayed


import random


def program():
    p1 = input("Enter your Choice: ")
    options = ["R", "S", "P"]
    p2 = random.choice(options)
    print("Computer chose " + p2)
    ch1 = p1.upper()
    ch2 = p2.upper()
    if ch1 == "R":
        if ch2 == "R":
            print("Tie!")
        elif ch2 == "P":
            print("Comp won!")
        elif ch2 == "S":
            print("You won!")
        else:
            print("Please use the keywords in the menu :-)")
        opinion()

    elif ch1 == "P":
        if ch2 == "R":
            print("You won !")
        elif ch2 == "P":
            print("Tie!")
        elif ch2 == "S":
            print("Comp won!")
        else:
            print("Please use the keywords in the menu :-)")
        opinion()

    elif ch1 == "S":
        if ch2 == "R":
            print("Comp Won!")
        elif ch2 == "P":
            print("You won!")
        elif ch2 == "S":
            print("Tie!")
        else:
            print("Please use the keywords in the menu :-)")
        opinion()

    else:
        print("Please use the keyword in the menu :-)")
        print("")
        program()


# def opinion is working good for all inputs
def opinion():
    print("")
    op = input("Do you wanna Continue? Y/N: ")
    print("")
    if op.lower() == "n":
        print("Have a nice day!")
        exit()
    elif op.lower() == "y":
        program()
    else:
        print("Please enter valid option from the menu: ")
        opinion()


# begin statements are working good for all inputs
def start():
    print("")
    print("Let's see who wins!.")
    print("Here's your menu:")
    print("")
    print("'Rock - R' , 'Paper - P' , 'Scissor - S' ")
    print("")

    begin = input("Shall we Start? Press Y to continue & any other key to exit:  ")
    print("")
    if begin.lower() == "y":
        program()

    else:
        print("")
        print("Thanks! Welcome back again")

# End of the file
