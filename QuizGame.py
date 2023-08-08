class Question:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer
# Add more questions here
def load_questions():
    questions = [
        Question("What is the capital of France?", ["A. London", "B. ROME ", "C. Paris", "D. Madrid"], "C"),
        Question("Which planet is known as the Red Planet?", ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"], "B"),
        Question("Which is largest animal on earth ALIVE?", ["A. Elephant", "B. Blue Whale", "C. Killer Whale", "D. WHITE SHARK"], "B"),
        
    ]
    return questions

def ask_question(question):
    print(question.question)
    for choice in question.choices:
        print(choice)
    user_answer = input("Your answer: ").upper()
    return user_answer

def QUIZ():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions by typing the letter corresponding to your choice.")
    
    questions = load_questions()
    total_questions = len(questions)
    correct_answers = 0

    for question in questions:
        user_answer = ask_question(question)
        if user_answer == question.correct_answer:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is {question.correct_answer}.\n")

    final_score = (correct_answers / total_questions) * 100
    print(f"Quiz completed!\nYour score: {final_score:.2f}%")

if __name__ == "__main__":
    QUIZ()
