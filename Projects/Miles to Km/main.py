from tkinter import *


def mile_to_km():
    miles_input=float(my_input.get())
    km=round(miles_input*1.609)
    answer.config(text=f"{km}")

window=Tk()
window.title("Miles to Kilometer")
window.minsize(height=150,width=200)
window.config(padx=20,pady=20)

my_input=Entry(width=7)
my_input.grid(row=0,column=1)

miles=Label(text="Miles")
miles.grid(row=0,column=2)

is_equal=Label(text="is Equal to")
is_equal.grid(row=1,column=0)

answer=Label(text="0")
answer.grid(row=1,column=1)

kilo=Label(text="Km")
kilo.grid(row=1,column=2)

button=Button(text="Calculate",command=mile_to_km)
button.grid(row=2,column=1)

window.mainloop()