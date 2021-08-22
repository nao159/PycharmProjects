class QuestionStruct:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        if self.question_number + 1 > len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}\n"
                            f"Is it True or False?").lower()
        self.check_answer(answer=user_answer, correct_answer=current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")
        print(f"The correct answer was {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}\n")


    def show_post_game_stats(self):
        print("The game is over!")
        percentage = (self.score / self.question_number) * 100
        print(f"You have {self.score} correct answers and {self.question_number - self.score} wrong answers. "
              f"You answer correctly at {percentage:.1f}% questions")
