class QuizBrain:
    def __init__(self, questions):
        self.score = 0
        self.question_num = 0
        self.question_list = questions

    def still_has_question(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        self.get_user_ans(current_question)

    def get_user_ans(self, current):
        user_ans = input(f"Q.{self.question_num}: {current.question}.(True/False)? ")
        self.check_ans(user_ans, current.answer)

    def check_ans(self, user_ans, right_ans):
        if user_ans.lower() == right_ans.lower():
            print("That's correct!")
            self.score += 1
        else:
            print("That's Wrong!")
            print(f"The correct answer was: {right_ans}")
        print(f"Your current score is: {self.score}/ {len(self.question_list)}\n")

