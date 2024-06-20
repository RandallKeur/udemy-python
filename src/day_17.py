""" Day 17 of Coding Challenges for True/False Quiz"""
from src.classes.quiz_generator import QuestionBank, Quiz


def take_quiz(question_bank: QuestionBank):
    questions = question_bank.select_n_questions()
    quiz = Quiz(questions)
    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")