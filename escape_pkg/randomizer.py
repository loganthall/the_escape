import random
from escape_pkg import all_options


def randomize_movement():  # function that randomizes the movement options
    # holds randomized movement selectors so that the original list is not mutated
    movement_options = []
    # holds randomized movement description that are aligned with the selectors so that the original list is not mutated
    movement_descriptions = []

    iter = 0  # sets iteration variable
    while iter < 3:  # iterates process of adding options to the non-global variables to allow 3 choices
        # generates random number to select index of an option/description set
        indexes = random.randint(0, len(all_options.movement_selectors) - 1)
        # checks for repeated items in the variable, skips without increasing iteration varibale if exists
        if all_options.movement_selectors[indexes] in movement_options:
            continue
        # appends randomly chosen item to the variable for user choice
        movement_options.append(all_options.movement_selectors[indexes])
        # checks for repeated items in the variable, skips without increasing iteration varibale if exists
        if all_options.movement[indexes] in movement_descriptions:
            continue
        # appends randomly chosen descriptions that are aligned with the users choice
        movement_descriptions.append(all_options.movement[indexes])

        iter += 1  # adds iteration to the loop

    iter = 0  # resets iteration variable
    while iter < 3:
        print(str(iter + 1), ". " + movement_options[iter])
        iter += 1

    # requests users choice of movement, and returns description accordingly
    user_choice = input("Choose your next move: ")
    if user_choice == "1":
        return movement_descriptions[0]
    elif user_choice == "2":
        return movement_descriptions[1]
    elif user_choice == "3":
        return movement_descriptions[2]
    elif user_choice in all_options.secret_words:  # if user enters a secret word, this happens
        print("\nYou spoke the secret word and the world around \nyou seems to materialize into something more familiar. \nYou slowly fade in and out of consciousness, and \nwhen you finally wake up you are back home \nin your bed. It was all a bad dream.")
        return False
    else:  # if nothing valid is entered, this is displayed
        print("\nPlease enter a valid choice.\n")
        return None


def randomize_actions():  # function to randomly choose, and randomly disperse, favorful or debilitating actions
    # chooses random number between 0 and 5 for the index of the action
    indexes = random.randint(0, len(all_options.random_actions) - 1)
    if indexes % 2 == 1:  # checks if index is even or odd. even indexes are null scenarios, so only odds have data
        if indexes == 5:
            consequence = "Your life has come to an untimely end.\n"
        elif indexes % 2 == 1:
            consequence = "You escape to the next area safely.\n"
        else:
            consequence = None
        return all_options.random_actions[indexes], consequence
    else:  # returns None for both variables if the index is even
        return None, None


def life_or_death():  # Function to randomize life or death when facing your foe
    coin = random.randint(0, 1)
    if coin == 0:  # if the coin toss lands on 0, the result is heads, which is living
        consequence = "heads"
        return consequence
    elif coin == 1:  # if the coin toss lands on 1, the result is tails, which is death
        consequence = "tails"
        return consequence


def play_again():  # function to ask user if they would like to play again or not
    play_again_choice = input("\nWould you like to play again? (y/n)")
    play_again_choice = play_again_choice.lower()  # converts input to lowercase for easier comparison
    if play_again_choice == "y" or play_again_choice == "yes":
        return True
    elif play_again_choice == "n" or play_again_choice == "no":
        print("\nThank you for playing.")
        return exit()
    else:
        print("\nPlease enter a valid option.")
        play_again()  # calls the function to run again if no valid input it entered
