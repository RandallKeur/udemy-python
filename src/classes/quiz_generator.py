"""Quiz that is generated for giving a quiz to the user"""
import random


class Question:
    # Disable too-few-public-methods error
    # pylint: disable=R0903
    """Models each question"""
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class QuestionBank:
    # Disable too-few-public-methods error
    # pylint: disable=R0903
    """Models the question banks"""
    def __init__(self, question_bank):
        self.questions = []
        for question in question_bank:
            new_question = Question(question['question'], question['answer'])
            self.questions.append(new_question)


class Quiz:
    """Models the quiz"""
    def __init__(self, question_bank: QuestionBank):
        self.question_bank = question_bank
        self.questions = []
        self.score = 0
        self.question_number = 0
        self.number_of_questions = 0

    def select_n_questions(self, number_of_questions: int):
        """Selects n questions from the question bank"""
        self.number_of_questions = number_of_questions
        max_questions = len(self.question_bank.questions)
        while self.number_of_questions > max_questions:
            print('Not enough questions in the question bank. Please try again.')
            self.number_of_questions = int(input('How many questions do you want on this quiz?: '))
        self.questions = random.sample(self.question_bank.questions, self.number_of_questions)

    def still_has_questions(self):
        """Checks if the quiz has questions remaining"""
        return self.question_number < self.number_of_questions

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
