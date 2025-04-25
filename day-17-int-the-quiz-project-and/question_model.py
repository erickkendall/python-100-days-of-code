class Question:
    """A class to represent a question in a quiz.
    
    Attributes:
        text (str): The text of the question.
        answer (str): The answer to the question (True/False).
    """
    
    def __init__(self, q_text, q_answer):
        """Initialize a Question object.
        
        Args:
            q_text (str): The text of the question.
            q_answer (str): The answer to the question.
        """
        self.text = q_text
        self.answer = q_answer
