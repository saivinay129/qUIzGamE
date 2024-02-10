from Quiz_pys.quiz_controler import *

# -------------------------- Quiz Start -----------------------------

print(f"""\033[96mWelcome to the Quiz!
There are {TOTAL_QUESTIONS} questions in the quiz\033[0m
""")

print(f"""\033[93mNote:-
--> You get +2 for a correct answer and -1 for a wrong answer.
--> All the answers are in true/false format.\033[0m
""")

print("\033[35mLet's Start!!\033[0m\n")

while True:

    question = Quiz(question_data[current_question - 1]['text'], question_data[current_question - 1]['answer']) # Create a Quiz object with the current question and answer from question_data.

    print(f"\nQuestion {current_question}: " + question.fetch_question())
    current_question, score = question.quiz_steps(current_question)

    if solving_passed_questions:
        current_question = -1 # Reset the current_question to -1 to manage passed questions.

    if current_question == 0: # Exit loop if user enters 'no' in next_question()
        break
    elif current_question == -1: # Checks if all questions are done
        if passed_questions_list: # Checks if there are any passed questions
            current_question = question.passed_questions()
            if not current_question: # Exit if user doesn't want to do any more passed questions
                break
        else: # Exit if there are no more questions to solve
            break


print("\n\033[93mQuiz Ended!\033[0m")
print(f"\033[93mFinal Score: {score}\033[0m")
# -------------------------- Quiz End -----------------------------