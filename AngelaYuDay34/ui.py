from tkinter import *

from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:


    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text=f"Score : {self.quiz.score}",font=("Courier",12,"roman"),bg=THEME_COLOR,fg="white")
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,text="",width=280 ,font=("Arial",20,"italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2, pady=50)

        self.true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true, highlightthickness=0, bg= THEME_COLOR, command=self.is_it_true)
        self.true_button.grid(row=2, column=0)

        self.false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false, highlightthickness=0, bg=THEME_COLOR, command=self.is_it_false)
        self.false_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        self.score_label.config(text=f"Score : {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_it_true(self):
        check = self.quiz.check_answer("true")
        self.give_feedback(check)

    def is_it_false(self):
        check = self.quiz.check_answer("false")
        self.give_feedback(check)

    def give_feedback(self, check):
        if check:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text,fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)
