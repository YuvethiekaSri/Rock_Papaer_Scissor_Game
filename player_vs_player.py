# This files has the code of playing with 2 players.
# It first asks for the name of the players and then for the choice from the menu.
# Based on the choice of the players, Winner is displayed

def program():
    p1 = input("Enter your Choice P1: ")
    p2 = input("Enter your Choice P2: ")
    ch1 = p1.upper()
    ch2 = p2.upper()
    if ch1 == "R":
        if ch2 == "R":
            print("Tie!")
        elif ch2 == "P":
            print(player2 + " won!")
        elif ch2 == "S":
            print(player1 + " won!")
        else:
            print("Please use the keywords in the menu :-)")
        opinion()

    elif ch1 == "P":
        if ch2 == "R":
            print(player1 + " won !")
        elif ch2 == "P":
            print("Tie!")
        elif ch2 == "S":
            print(player2 + " won!")
        else:
            print("Please use the keywords in the menu :-)")
        opinion()

    elif ch1 == "S":
        if ch2 == "R":
            print(player2 + " Won!")
        elif ch2 == "P":
            print(player1 + " won!")
        elif ch2 == "S":
            print("Tie!")
        else:
            print("Please use the keywords in the menu :-)")
        opinion()

    else:
        print("Please use the keywords in the menu :-)")
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
    begin = input("Shall we Start? Press Y to continue & any other key to exit:  ")
    print("")
    if begin.lower() == "y":
        program()
    else:
        print("")
        print("Thanks! Welcome back again")

# End of the file

print("Let's see who wins!.")
print("Here's your menu:")
print("")
print("'Rock - R' , 'Paper - P' , 'Scissor - S' ")
print("")
player1 = input("Player1 name: ")
player2 = input("Player2 name: ")
print("")
start()