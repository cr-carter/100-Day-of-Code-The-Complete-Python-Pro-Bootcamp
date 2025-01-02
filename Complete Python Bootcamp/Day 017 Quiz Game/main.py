# The purpose of this project is to practice creating classes, working with dictionaries,
# and using for loops to loop through dictionaries. I also am gaining experience importing
# classes, lists, etc. from other sources. Lastly, I gained practice importing and converting
# jsons to dictionary items.

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    question_bank.append(Question(question_text, question_answer))

print(question_bank)

quiz = QuizBrain(question_bank)

print(f"Answer the following {len(quiz.question_list)} true/false questions.\n")

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

