import random

from flask import Flask

app = Flask(__name__)

GUESS=random.randint(1,10)


def make_style(func):
    def wrapper(*args,**kwargs):
        return f"<center> <b> {func(*args,**kwargs)} </b> </center>"
    wrapper.__name__=func.__name__
    return wrapper




@app.route("/")
@make_style
def home():
    return '<h1>Guess a number between 1 and 10</h1>'\
            '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2J5YWxwbzR2aXYzcXBnY2g2YzJ6dDJ3cWVqY2Y0eDJwbHV5bWIwdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/i7PM4udF7hrjzmojpd/giphy.gif">'


@app.route("/<int:number>")
@make_style
def guess_number(number):
    if number > GUESS :
        return '<h1>Too high, Enter Less Value</h1>'\
                '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXJ0a2ttaDh0bGRwcDR2M2hqN3ZscndlZnF5MWhuM2h1OTNkc3E1NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3og0IuWMpDm2PdTL8s/giphy.gif">'
    elif number < GUESS:
        return '<h1>Too Low, Enter High Value</h1>' \
               '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTZlZXpmM3dveXEyaG96emd3YWZxMnJybnhsNXdsNGIybXRzYzh6cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SIfresLBpFtsI9Wc4F/giphy.gif">'
    else:
        return '<h1>You are Right</h1>' \
               '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTh2ZDRla3kxdmhsanR4NzJpbGl3N3l3a2x5OTZhN2w2dHloNnQ3ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uVpPvvpU3nip5pBkPD/giphy.gif">'


if __name__=="__main__":

    app.run(debug=True)