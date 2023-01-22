# the_escape
Fundamentals of Python course personal project
Text-based Choose Your Own Path Adventure

This project highlights the using of random integer creations for the illusion of full user autonomy in their choices.

As the game begins, you will be greeted by the scenario. From then, you begin making choices,
randomized from pre-set lists. Each choice has a description of the choice, and there is always a random
possibility of something helpful, or horrible, happening. After making it safely between rooms 10 times, you are
automatically led to the exit, and your life is spared. There are also a set of keywords that can be found
through playing that, when entered, are instant win conditions.

At the beginning of the development process, I wrote down many options for movement selections,
their descriptions, the random situations, and the secret words. The next step was to decide how I wanted the
options to be selected and implemented. Being as simple as it was, I opted not to use a flowchart to show the
flow of the game at this point.

After I had the options laid out, I created a module file that contained all of the data types and values. I
originally opted to use Dictionaries and Tuples as some of the data was related and some needed to be
immutable. But my initial implementation was not forgiving in the way of pulling the data and displaying it
properly, so I changed several to Lists and left one as a Set. Upon refactoring, I realized I could make them all
as Tuples, so I changed them, except the values of the secret words which is a Set, eliminating the possibility
that I would accidentally change a value in one and throw off the entire flow of the game.
![Screenshot](https://github.com/loganthall/the_escape/blob/a72c2cb50fa2a8baaf42adf274f7c228a9b4ca0c/screenshots/the-escape-1.png)

There are 2 Tuples that are related to each other. I initially tried using a dictionary for this, but the
process became more tedious and unreliable the more I wrote the code to access them, so I opted to separate
them for this implementation. I made sure to place the related items in the same indexes on each Tuple so that
one iteration could catch them both.

My next thought was to determine how I wanted each part of the user interaction to be handled. I knew
that I would need the user to enter their choice for action, so I started writing a function to display random
action options, handle the user input, and return the result. I created a new file as a module in the package to
contain all of the core functions. Using a List type, I wrote a while loop that iterates 3 times through the
movement action Tuples, pulling random choices to the accompanying Lists, and checking for duplicates to
make sure the same options don't appear for each round of choices. It then pulls the user input, checks it
against the secret words and if it is a valid input, then displays the result which is the index in the list that was
chosen by the user. This function essentially took me the most time of the project, as I kept changing data
types, and experimenting with how to manipulate and call them properly.
![Screenshot](https://github.com/loganthall/the_escape/blob/a72c2cb50fa2a8baaf42adf274f7c228a9b4ca0c/screenshots/the-escape-2.png)

Moving forward, the next thing I wanted to handle was the randomization of helpful or horrible actions
that happen, and each of those actions creates a random life or death coin flip. These functions randomly
choose the index correlated to the random happenstances, and the life or death scenario. For the random
happenings, the Tuple is created such that every odd number is associated with a scenario, and every even
number is a free pass and nothing happens. This was my first time implementing modulus operations in my
python programming, but it was a welcome addition. In the current version of the game, only index 5 out of all 6
of the options provides an instant death scenario every time. The life_or_death() function is called whenever
the option to turn around and face your assailant is chosen. So you have a 50% chance of either choice.
![Screenshot](https://github.com/loganthall/the_escape/blob/a72c2cb50fa2a8baaf42adf274f7c228a9b4ca0c/screenshots/the-escape-3.png)

At this point, I needed to provide an option to play the game again, which is where the play_again()
function comes in. At any point when the game ends, either by life or death, the option to play again needs to
be provided. Again, the user is asked to enter their choice, and given the parameters, y or n. The if conditional
checks to make sure that either y or n, or even yes or no, was entered. If the no option is selected, an
appropriate message is displayed and the game is forcefully closed by using the built-in exit() method. If a yes
option is entered, this function returns true, which will make sense when explaining the main file. If no proper
choice was given, the function is called again and the user is asked to enter a valid option.
![Screenshot](https://github.com/loganthall/the_escape/blob/a72c2cb50fa2a8baaf42adf274f7c228a9b4ca0c/screenshots/the-escape-4.png)

Now that the modules were finished, I moved my sights to the main file that would run the entire show. I
decided on putting the entire code into a while loop so that the play_again() functionality was much easier to
work with. This is where the “return True” portion of that function comes into play. To begin, I added the starting
“graphic” intro, with a user input that goes nowhere, just to allow the user to start the game when they want
and not get thrown in immediately. The “r” at the beginning of the print statement denotes that the following
lines are raw input, and should not be analyzed as code.
![Screenshot](https://github.com/loganthall/the_escape/blob/a72c2cb50fa2a8baaf42adf274f7c228a9b4ca0c/screenshots/the-escape-5.png)

The next part of the code I added, since it would be one of the simpler parts, was the instant win after
an amount of "time". After every choice, an iteration counter goes up, counting the ”rooms” you have completed.
At 10, you are an instant winner.
![Screenshot](https://github.com/loganthall/the_escape/blob/a72c2cb50fa2a8baaf42adf274f7c228a9b4ca0c/screenshots/the-escape-6.png)

The next step in the flow was calling the choice randomization, and then working with the output. If the
output returns false, which would be done if a secret word was typed in, the appropriate message is displayed,
and the play_again function is called, which if True(yes), the game restarts. Next, if the choice returned None,
which would happen if an invalid input was entered, the appropriate “try again” message is displayed , the
room counter is decremented to show that the room had not been passed, and the loop starts again.
![Screenshot](https://github.com/loganthall/the_escape/blob/a72c2cb50fa2a8baaf42adf274f7c228a9b4ca0c/screenshots/the-escape-7.png)

Following the None return, we get into the meat of the selections. If the choice input is a valid selection,
the corresponding description for the choice is displayed. Then, if a specific choice is chosen, the life or death
coin flip is immediately run. If heads, you survive and make it to the next turn. If tails, you die and lose the
game. After that check, the random turn actions are run. When the action returns as None or an empty string,
which is caused by the random index being even since evens have no action, the while loop is continued which
causes the next turn to immediately begin. Otherwise, the action is passed to the variable, and the action
consequence is run. The consequence will be that the user lives UNLESS the action was index 5, which is an
instant death. Even number indexes cause the consequence to pass back None, which prints back only the
action. Odd number actions that aren’t 5 will cause a return that prints the death message and the play again
method. Finally, if none of the above are true, it will return back the action and the consequence. That is the
end of the functioning code. Where it is all in the while loop, it will all continue to run until certain actions cause
a break in the loop to end the game.
![Screenshot](https://github.com/loganthall/the_escape/blob/a72c2cb50fa2a8baaf42adf274f7c228a9b4ca0c/screenshots/the-escape-8.png)

In conclusion, this project has forced me to stop and think many times about the way I am doing certain
actions and if they could be done more efficiently or in a less computationally intensive manner. The multiple
variables and data types I created to house the related data could most likely have benefited from being made
into a dictionary and called more efficiently. Working through data input and validation has been challenging,
but fun, and I know as I further my study into the language I will find ways to write better code. If I were to
come back to this program in the future, I believe I would add a Stack data type so that the user could
backtrack through the rooms and their choices, and possibly add more actions and choices with a damage
system.
