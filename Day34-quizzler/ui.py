from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR: str  # Type hint
THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quiz Time')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Score and scoreboard
        self.scoreboard = Label(text=f"Score: {self.quiz.score:>02}", font=('Arial', 12, 'normal'), bg=THEME_COLOR, fg='#fff')
        self.scoreboard.grid(row=0, column=1)

        self.canvas = Canvas(height=200, width=400)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(
            200,
            100,
            width=360,
            text="This is here question goes.",
            font=('Arial', 14, 'italic'),
            fill=THEME_COLOR)

        # Buttons
        self.false_btn = Button(text='False', font=('Arial', 12, 'bold'), width=8, height=1, bg='#FF6D60', fg='white',
                                command=self.f_ans)
        self.false_btn.grid(row=2, column=0)
        self.true_btn = Button(text='True', font=('Arial', 12, 'bold'), width=8, height=1, bg='#98D8AA', fg='white',
                               command=self.t_ans)
        self.true_btn.grid(row=2, column=1)

        self.update_score()
        self.get_next_question()
        self.window.mainloop()

    def update_score(self):
        self.scoreboard.config(text=f"Score: {self.quiz.score:>02}")

    def f_ans(self):
        self.feedback(self.quiz.check_answer('False'))

    def t_ans(self):
        self.feedback(self.quiz.check_answer('True'))
        self.update_score()

    def get_next_question(self):
        self.canvas.config(bg='#fff')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz."
                                        f"\nYour final score is: {self.quiz.score:>02}/{self.quiz.question_number}")
            self.false_btn.config(state='disabled')
            self.true_btn.config(state='disabled')

    def feedback(self, result):
        if result:
            self.canvas.config(bg='#98D8AA')
        else:
            self.canvas.config(bg='#FF6D60')

        self.window.after(100, self.get_next_question)

