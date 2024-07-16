""" Day 17 of Coding Challenges for True/False Quiz"""
from src.classes.quiz_generator import QuestionBank, Quiz


def take_quiz(question_bank: QuestionBank):
    """ Takes a question bank and has the user start a quiz"""
    quiz = Quiz(question_bank)
    number_of_questions = int(input("How many questions do you want on this quiz?: "))
    quiz.select_n_questions(number_of_questions)
    while quiz.still_has_questions():
        quiz.next_question()

    print("You\'ve completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
