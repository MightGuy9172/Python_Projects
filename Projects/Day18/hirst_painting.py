#Hirst Painting
import turtle as t
import random
import colorgram


t.colormode(255)
teddy=t.Turtle()
teddy.speed("fastest")

colors=colorgram.extract("image.jpg",40)
rgbColors=[]
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    newColor=(r, g, b)
    rgbColors.append(newColor)

teddy.penup()
teddy.hideturtle()
teddy.setheading(225)
teddy.forward(300)
teddy.setheading(0)
dots=100
teddy.dot(20,random.choice(rgbColors))
for dot in range(1,(dots+1)):
    teddy.dot(20,random.choice(rgbColors))
    teddy.forward(50)

    if dot%10==0:
        teddy.setheading(90)
        teddy.forward(50)
        teddy.setheading(180)
        teddy.forward(500)
        teddy.setheading(0)


screen=t.Screen()
screen.exitonclick()

