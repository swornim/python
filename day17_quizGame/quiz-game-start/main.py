from  question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for key in question_data:
    new_q = Question(key["text"],key["answer"])
    question_bank.append(new_q)

q_brain = QuizBrain(question_bank)
while q_brain.still_has_questions():
    q_brain.next_question()

print("you've completed the quiz")
print(f"Your final score was : {q_brain.score}/{q_brain.question_number}")