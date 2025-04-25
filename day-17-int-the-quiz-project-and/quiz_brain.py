class QuizBrain:
    """A class to manage the quiz logic.
    
    Attributes:
        question_number (int): The current question number.
        question_list (list): List of Question objects.
        score (int): The current score.
    """

    def __init__(self, q_list):
        """Initialize a QuizBrain object.
        
        Args:
            q_list (list): List of Question objects.
        """
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        """Display the next question and check the user's answer."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """Check if there are still questions left in the quiz.
        
        Returns:
            bool: True if there are still questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """Check if the user's answer is correct.
        
        Args:
            user_answer (str): The user's answer.
            correct_answer (str): The correct answer.
        """
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def final_score(self):
        """Display the final score."""
        print(f"Your final score is: {self.score}/{self.question_number}")
