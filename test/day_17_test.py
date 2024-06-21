"""Test for Day 17 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.classes.quiz_generator import QuestionBank, Quiz
from src.constants.question_bank import QUESTION_BANK
from src.day_17 import take_quiz


class Day17Test(unittest.TestCase):
    """Test for Day 17 of Coding"""
    def setUp(self):
        self.question_bank = QuestionBank(QUESTION_BANK)
        self.quiz = Quiz(self.question_bank)
        self.number_of_questions = 0
        self.out = StringIO()
        sys.stdout = self.out

    def test_quiz_with_10_questions(self):
        """Test the coffee machine espresso with change"""
        # given
        self.number_of_questions = 10
        self.quiz.select_n_questions(self.number_of_questions)
        expected = 'Your final score was: '
        with mock.patch('sys.stdin', new=StringIO(f'{self.number_of_questions}\nTrue\nTrue\nTrue\n'
                                                  f'True\nTrue\nTrue\nTrue\nTrue\nTrue\nTrue')):

            # when
            take_quiz(self.question_bank)
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(expected in actual)


if __name__ == '__main__':
    unittest.main()
