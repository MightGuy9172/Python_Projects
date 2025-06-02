
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#E38CB2"
RED = "#EC2655"
GREEN = "#6CE58A"
YELLOW = "#F8F2AD"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timeText, text="00:00")
    heading.config(text="Timer")
    done.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def startTimer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps%8==0:
        count_down(long_sec)
        heading.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(short_sec)
        heading.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        heading.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minutes=math.floor(count/60)
    seconds=count%60

    if seconds<10:
        seconds=f"0{seconds}"

    canvas.itemconfig(timeText,text=f"{minutes}:{seconds}")
    if count>0:
        timer=window.after(1000,count_down,count-1)
    else:
        startTimer()
        workSession=math.floor(reps/2)
        mark=""
        for _ in range(workSession):
            mark+="✔"
        done.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

window.after(1000,)

heading=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))
heading.grid(row=0,column=1)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
timeText=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

start=Button(text="Start",highlightthickness=0,command=startTimer)
start.grid(row=2,column=0)

reset=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(row=2,column=2)

done=Label(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
done.grid(row=3,column=1)

window.mainloop()