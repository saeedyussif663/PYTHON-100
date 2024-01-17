class QuizBrain:

    def __init__ (self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_question_text = current_question.text
        current_question_answer = current_question.answer
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question_text} (True/False): ")
        self.check_answer(answer, current_question_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("You are Wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
