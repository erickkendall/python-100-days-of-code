# Day 17 - The Quiz Project & the Benefits of OOP
# 100 Days of Code - Python Pro Bootcamp

"""
Main module for the Quiz Project. This script creates a quiz from questions
fetched from the Open Trivia Database API and runs the quiz using the QuizBrain class.
"""

from question_model import Question
from quiz_brain import QuizBrain
from trivia_api import get_trivia_questions


def create_question_bank():
    """Create a list of Question objects from the Open Trivia Database API.
    
    Returns:
        list: A list of Question objects.
    """
    # Fetch fresh questions from the API
    question_data = get_trivia_questions(amount=10, question_type="boolean")
    
    questions = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        
        new_question = Question(question_text, question_answer)
        questions.append(new_question)
    
    return questions


def main():
    """Run the quiz program."""
    question_bank = create_question_bank()
    
    # Check if we got any questions
    if not question_bank:
        print("Unable to fetch questions. Check your internet connection.")
        return
    
    quiz = QuizBrain(question_bank)
    
    while quiz.still_has_questions():
        quiz.next_question()
    
    quiz.final_score()


if __name__ == "__main__":
    main()
