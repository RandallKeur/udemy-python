"""Quiz that is generated for giving a quiz to the user"""
from src.constants.question_bank import QUESTION_BANK
import random


class Question:
    """Models each question"""
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class QuestionBank:
    """Models the question banks"""
    def __init__(self):
        self.questions = []
        for question in QUESTION_BANK:
            new_question = Question(question['question'], question['answer'])
            self.questions.append(new_question)

    def select_n_questions(self):
        """Selects n questions from the question bank"""
        max_questions = len(self.questions)
        number_of_questions = max_questions + 1
        while max_questions < number_of_questions:
            number_of_questions = int(input('How many questions do you want on this quiz?: '))
            if number_of_questions > max_questions:
                print('Not enough questions in the question bank. Please try again.')
        return random.sample(self.questions, number_of_questions)


class Quiz:
    """Models the quiz"""
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_number = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def next_question(self):
        """Gets the next question on the quiz"""
        current_question = self.questions[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.question} (True/False): ')
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks if the answer is correct"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print('That\'s wrong.')
        print(f'The correct answer was: {correct_answer}.')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print('\n')

