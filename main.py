# This is the code to choose the mode of play
print("")
print("Enter 1 to play with computer.")
print("Enter 2 to play with another player.")
print("")
ch = int(input("Choose the mode of play: "))


# This function takes the user choice and then import the python files to proceed


def choices(ch):
    if ch == 1:
        import player_vs_computer
        player_vs_computer.start()

    elif ch == 2:
        import player_vs_player
        # This imports and run the file player_vs_player

    else:
        print("Enter a valid choice from the menu.")
        print("")


choices(ch)
# Program main ends here.
