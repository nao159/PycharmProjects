from data import text_question_data
from question_model import Question
from question_structure import QuestionStruct

question_bank = []

for question in text_question_data:
    q = Question(q_text=question["question"], q_answer=question["correct_answer"])
    question_bank.append(q)

print(len(question_bank))
quiz = QuestionStruct(question_list=question_bank)
while quiz.still_has_question():
    quiz.next_question()
quiz.show_post_game_stats()