from Quiz_pys.quiz_blueprint import *

TOTAL_QUESTIONS = len(question_data)

passed_questions_list = []
questions_solved = 0
score = 0
solving_passed_questions = False

class Quiz(Questions):

    def __init__(self, question_text, correct_answer):

        super().__init__(question_text, correct_answer) # Initialize the Quiz object by calling the constructor of the parent Questions class.



    def next_question(self): # Method to handle moving to the next question.

        global current_question

        if current_question >= TOTAL_QUESTIONS: 
            return -1 # Return -1 if all the questions have been answered

        move_to_next_question = (input("Move on to the next question? (y/n): ")).strip()[0].lower()

        while move_to_next_question not in ['y', 'n']:
            print("Invalid Input!!")
            move_to_next_question = (input("Move on to the next question? (y/n): ")).strip()[0].lower()
        
        if move_to_next_question == 'n':
            return 0 # Return 0 if user doesn't want to move to next question

        current_question += 1
        return current_question

    def user_answer(self): # Method to get the user's answer to a question.

        your_answer = input("\nYour Answer (True/False/Pass): ").strip()[0].upper()
        while your_answer not in ['T', 'F', 'P']:
            print("Invalid Input!!")
            your_answer = input("Your Answer (True/False/Pass): ").strip()[0].upper()
        
        return your_answer

    def check_answer(self, your_answer, current_question): # Method to check if the user's answer is correct and update the score.

        
        global questions_solved, score

        if your_answer != 'P': # Checks if the user didn't pass the question
            if your_answer == self.fetch_answer()[0].upper():
                print("\033[92mCorrect!! You gain 2 points.\033[0m")
                score += 2
            else:
                print("\033[91mWrong :(  You lost 1 point\033[0m")
                score -= 1
            questions_solved += 1
            print(f"{self.questions_remain()} questions remain.")
        else:
            passed_questions_list.append(current_question) # If passed then add current question to passed_question_list
        
        return score

    def quiz_steps(self, current_question): # Method containing steps for each quiz question
        
        your_answer = self.user_answer()
        score = self.check_answer(your_answer, current_question)
        current_question = self.next_question()
        return current_question, score

    def questions_remain(self): # Method to calculate the number of questions remaining

        return TOTAL_QUESTIONS - questions_solved
    
    def passed_questions(self): # Method to handle passed questions
        
        global solving_passed_questions

        print("\nQuestions Passed: ", sorted(passed_questions_list))

        current_question = int(input("Select a question you want to do or press 0 to quit: "))
        while current_question not in passed_questions_list and current_question != 0:
            print("Invalid Input. Enter the correct question number!")
            current_question = int(input("Select a question you want to do or press 0 to quit: "))
        if current_question:
            passed_questions_list.remove(current_question) # Remove the question from the list if it has been solved
            solving_passed_questions = True
            return current_question
        else:
            return 0 # Return 0 if user decides to quit