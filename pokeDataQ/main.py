from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
states = 50
correct_guesses = 0
guesses_states = []
screen.title("USA States")
screen.bgpic("blank_states_img.gif")

state_list = pd.read_csv("50_states.csv")
state_name_list = state_list.state


def guess_state(answer):
    for state in state_name_list:
        global guesses_states
        if answer == state and answer_state not in guesses_states:
            global correct_guesses
            correct_guesses += 1
            guesses_states.append(answer)
            current_state = state_list[state_name_list == answer]
            x = int(current_state.x)
            y = int(current_state.y)
            new_turtle = Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.goto(x, y)
            new_turtle.write(answer)
            break


def is_exit(answer):
    global game_is_on
    if answer == "Exit":
        states_to_learn = state_name_list.to_list()
        for state in guesses_states:
            states_to_learn.remove(state)
        while len(guesses_states) > len(states_to_learn):
            states_to_learn.append("")
        while len(guesses_states) < len(states_to_learn):
            guesses_states.append("")
        new_dict = {
            "Correctly guessed": guesses_states,
            "Missing:": states_to_learn
        }

        new_data = pd.DataFrame(new_dict)
        new_data.to_csv("result.csv")
        game_is_on = False


game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{correct_guesses} / {states}", prompt="whats state name").title()
    is_exit(answer=answer_state)
    guess_state(answer=answer_state)


screen.exitonclick()
