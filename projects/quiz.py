import random

# Sample quiz data
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Berlin", "D. Madrid"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    }
]

def run_quiz(quiz):
    score = 0
    random.shuffle(quiz)
    for question in quiz:
        print(question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {question['answer']}.\n")
    print(f"You scored {score} out of {len(quiz)}.")

# User profile
user_name = input("Enter your name: ")
print(f"Welcome to the Quiz App, {user_name}!")

# Run the quiz
run_quiz(quiz)
