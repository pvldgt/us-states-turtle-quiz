import turtle
import pandas
from state_write import Writer

# create the screen and set the background to the US map
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# create the writer from the Writer class
writer = Writer()

# keep the score of the correctly guessed states
correct_count = 0
# keep the record of the correctly guessed states
guessed_states = []
# turn the 50 states record into a data frame and then create a list of all the states
df = pandas.read_csv("50_states.csv")
list_of_states = df["state"].tolist()
# a list of states that the user didn't guess correctly
list_of_states_to_learn = []

# while loop to keep the game going until one reaches 50 states counter or types 'exit'
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{correct_count}/50 Guess the state",
                                    prompt="Enter another state's name").title()
    # check if the answer is in the list of states
    # if it is then add +1 to counter and add the state to the guessed_states list
    # also write the name of the state on the map in the right place using the x and y coordinates
    # taken from the data frame
    if answer_state in list_of_states and answer_state not in guessed_states:
        correct_count += 1
        guessed_states.append(answer_state)
        xcor = df[df.state == answer_state].x.item()
        ycor = df[df.state == answer_state].y.item()
        writer.write_on_screen(answer_state, xcor, ycor)

    # if the user guesses all 50 states, finish the game and display a winning message
    if correct_count == 50:
        game_is_on = False
        writer.game_over()

    # if the user gives up and types 'exit', finish the game, display the message and
    # create a csv file from the list of states that were not guessed
    if answer_state == "Exit":
        for state in list_of_states:
            if state not in guessed_states:
                list_of_states_to_learn.append(state)
        state_dict = {"State": list_of_states_to_learn}
        data = pandas.DataFrame(state_dict)
        data.index += 1
        data.to_csv("States_to_learn.csv")
        writer.finish_game()
        game_is_on = False

screen.mainloop()