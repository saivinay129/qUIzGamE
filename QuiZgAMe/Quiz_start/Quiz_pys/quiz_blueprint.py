from Quiz_pys.quiz_questions import question_data

current_question = 1 # Initialize current question counter

class Questions:

    def __init__(self, question_text, correct_answer):
        self.question_text = question_text 
        self.correct_answer = correct_answer 

    def fetch_question(self):
        return self.question_text # Method to return the question text

    def fetch_answer(self):
        return self.correct_answer # Method to return the correct answer of the question