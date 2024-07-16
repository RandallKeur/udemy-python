"""Test for Day 17 of Coding Challenges"""
import random
import sys
import unittest
from io import StringIO
from unittest import mock

from src.classes.quiz_generator import QuestionBank, Quiz
from src.constants.values import QUESTION_BANK
from src.day_17 import take_quiz


class Day17Test(unittest.TestCase):
    """ Test for Day 17 of Coding"""

    def setUp(self):
        self.question_bank = QuestionBank(QUESTION_BANK)
        self.quiz = Quiz(self.question_bank)
        self.number_of_questions = random.randint(1, len(self.question_bank.questions))
        self.out = StringIO()
        sys.stdout = self.out

    def test_quiz_with_n_questions_all_true(self):
        """ Test the coffee machine espresso with change"""
        # given
        self.quiz.select_n_questions(self.number_of_questions)
        expected = 'Your final score was: '
        n_answers = '\nTrue' * self.number_of_questions
        with mock.patch('sys.stdin', new=StringIO(f'{self.number_of_questions}{n_answers}')):
            # when
            take_quiz(self.question_bank)
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(expected in actual)

    def test_quiz_with_n_questions_all_false(self):
        """ Test the coffee machine espresso with change"""
        # given
        self.quiz.select_n_questions(self.number_of_questions)
        expected = 'Your final score was: '
        n_answers = '\nFalse' * self.number_of_questions
        with mock.patch('sys.stdin', new=StringIO(f'{self.number_of_questions}{n_answers}')):
            # when
            take_quiz(self.question_bank)
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(expected in actual)

    def test_quiz_with_n_questions_random_answers(self):
        """ Test the coffee machine espresso with change"""
        # given
        self.quiz.select_n_questions(self.number_of_questions)
        expected = 'Your final score was: '
        n_answers = f'\n{random.choice(['True', 'False'])}' * self.number_of_questions
        with mock.patch('sys.stdin', new=StringIO(f'{self.number_of_questions}{n_answers}')):
            # when
            take_quiz(self.question_bank)
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(expected in actual)


if __name__ == '__main__':
    unittest.main()
