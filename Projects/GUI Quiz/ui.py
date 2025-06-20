from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain

        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)

        self.score=Label(text=f"Score: 0",fg="white",bg=THEME_COLOR,font=("Arial",15,"bold"))
        self.score.grid(column=1,row=0)

        self.canvas=Canvas(height=250,width=300,bg="White")
        self.question_text=self.canvas.create_text(150,125,
                                text="Some Question",
                                width=280,
                                font=("Arial",18,"italic"),fill=THEME_COLOR)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        false_img=PhotoImage(file="images/false.png")
        self.false_button=Button(image=false_img,highlightthickness=0,command=self.check_false)
        self.false_button.grid(row=2,column=0)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img,highlightthickness=0,command=self.check_true)
        self.true_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've Reached the End of Quiz !")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_false(self):
        is_right=self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def check_true(self):
        is_right=self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
