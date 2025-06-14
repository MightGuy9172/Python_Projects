from turtle import Turtle

ALIGN="center"
FONT=("Arial", 24, "normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.point=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f" Score= {self.point} High Score= {self.high_score}", align=ALIGN, font=FONT)

    def inc_score(self):
        self.point+=1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)

    def reset(self):
        if self.point>self.high_score:
            self.high_score=self.point
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.point=0
        self.update_score()
