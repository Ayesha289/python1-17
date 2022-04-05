from day17data import question_data

class Question:
    def __init__(self, text, answer):
        self.question = text 
        self.answer = answer

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

class QuizBrain:
    def __init__(self, text):
        self.question_number = 0
        self.score = 0
        self.question_list = text
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}.: {current_question.question} (True/False)?: ").title()
        self.check_answer(answer, current_question.answer)
    
    def still_has_questions(self):
        if len(question_data) > self.question_number:
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        score = 0
        if user_answer.title() == correct_answer:
            print("You got it right!")
            self.score += 1
            print(f"Your current score is: {self.score}/{self.question_number}!")
        else:
            print("That's wrong.")
            print(f"Your final score is: {self.score}/{self.question_number}.")
        print(f"The correct answer was {correct_answer}.\n\n")

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")