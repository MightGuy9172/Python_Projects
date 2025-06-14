import turtle
from turtle import Turtle, Screen
import random
import tkinter.messagebox as msgbox  # Import messagebox from tkinter

race = False
screen = Screen()
screen.setup(width=500, height=500)

userInput = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? red, yellow, orange, green, blue, purple")
colors = ["red", "yellow", "orange", "green", "blue", "purple"]
yPos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=yPos[i])
    all_turtles.append(new_turtle)

if userInput:
    race = True

while race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race = False
            win_color = turtle.pencolor()
            if win_color == userInput:
                msgbox.showinfo("Result", f"You Win! The {win_color} turtle is the Winner!")
            else:
                msgbox.showinfo("Result", f"You Lost! The {win_color} turtle is the Winner!")
            break
        distance = random.randint(1, 10)
        turtle.forward(distance)

screen.exitonclick()
