import pandas
import turtle

screen=turtle.Screen()
screen.title("Indian State Guess")
image="india_map.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("28_states.csv")
all_state=data.state.to_list()
guessed=[]
while len(guessed)<28:
    answer=screen.textinput(title=f"{len(guessed)}/28 Guessed State",prompt="Guess any Indian State name?").title()

    if answer=="Exit":
        missing=[state for state in all_state if state not in guessed]
        new_data=pandas.DataFrame(missing)
        new_data.to_csv("state_to_learn.csv")
    if answer in all_state:
        guessed.append(answer)
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data=data[data.state==answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())




