"""
Python Fundamentals - Personal Project
Logan Hall
1/20/23
info.tech.logan@gmail.com
"""

# calls the module that runs the randomization for the game
from escape_pkg import randomizer
from escape_pkg import all_options

while True:
    # Sets iterarion varible for amount of time the game loop has run. Also acts as a Room counter.
    iter = 0

    print("\n-=-=-=-=-=-=-=-=-= Welcome to The Escape =-=-=-=-=-=-=-=-=-")
    input("-=-=-=-=-=-=-=-=-= Press ENTER to Begin  =-=-=-=-=-=-=-=-=-\n")

    print("Your story begins in a dimly lit room. Head pounding. Heart racing. Nose bleeding.\nAs you sit up from your slumber, you notice you aren't anywhere that looks familiar.\nWithout warning, the sound of a chainsaw starts and comes barging into the room.\nThe choices you make next may save your life.\nChoose your moves wisely.\n")

    while iter >= 0:
        iter += 1  # increments iteration/room counter by 1 each loop

        if iter > 10:  # after 10 successful choices, the user makes it out alive
            print("\nYou finally come to a door that appears to be barred shut. Fortunately, there is an open window above it, just big enough for your body to slip through. You climb up into the windows with all your remaining strength, and fall to the other side, feeling the warmth of daylight hit your face. The nightmare is over...you have survived.")
            play_again = randomizer.play_again()
            if play_again == True:
                    break

        # provides indication of how far the user has gotten
        # print("Room:", iter)
        # displays random movement options, and asks for user choice
        movement_choice = randomizer.randomize_movement()
        if movement_choice == False:  # Flase is returned when a secret word is entered
            play_again = randomizer.play_again()
            if play_again == True:
                break
        elif movement_choice == None:  # None is returned when invalid input is entered
            iter -= 1
            continue
        else:
            print(movement_choice)  # outputs the movement choice description

            # if the user chooses the following option at any time, a random life or death choice is made
            if movement_choice == "\nYou decide to turn around and face the one that brought you here. Not only are they larger than you, their eyes somehow glow black with darkess.\n":
                life_or_death = randomizer.life_or_death()
                if life_or_death == "heads":  # continues play if heads is randomly selected
                    print(all_options.random_actions[1], "\n")
                    print("You escape to the next area safely.\n")
                    continue
                elif life_or_death == "tails":  # ends game if tails is randomly selected
                    print(all_options.random_actions[5], "\n")
                    print("Your life has come to an untimely end.\n")
                    play_again = randomizer.play_again()
                    if play_again == True:
                        break

            # sets the two variables to the two outputs of the function
            action, consequences = randomizer.randomize_actions()
            if action is None or action == "":  # if there is no random action selected, the loop is reset from this point and no random action is displayed
                continue
            if consequences == "none":  # if an action is randomly selected, but a no consequence is randomly selected, print only the action
                print(action)
            # if this particular consequence gets selected, display bot the action and consequence
            elif consequences == "Your life has come to an untimely end.\n":
                print(action, consequences)
                play_again = randomizer.play_again()
                if play_again == True:
                    break
            else:
                print(action, consequences)
