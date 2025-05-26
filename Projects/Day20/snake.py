from turtle import Turtle

POS=[(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.my_turtle = []
        self.create_snake()
        self.head=self.my_turtle[0]

    def create_snake(self):
        for i in POS:
           self.add_segment(i)

    def add_segment(self,position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.my_turtle.append(new_turtle)

    def reset(self):
        for segment in self.my_turtle:
            segment.goto(1000,1000)
        self.my_turtle.clear()
        self.create_snake()
        self.head = self.my_turtle[0]

    def extend(self):
        self.add_segment(self.my_turtle[-1].position())


    def move(self):
        for segment in range(len(self.my_turtle) - 1, 0, -1):
            x_cor = self.my_turtle[segment - 1].xcor()
            y_cor = self.my_turtle[segment - 1].ycor()
            self.my_turtle[segment].goto(x_cor, y_cor)

        self.my_turtle[0].forward(MOVE_DIS)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)