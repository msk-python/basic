import random

quiz = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 4"],
        "answer": "B"
    },
    {
        "question": "Which method is used to add an element to the end of a list?",
        "options": ["A. append()", "B. add()", "C. insert()", "D. extend()"],
        "answer": "A"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": ["A. .pyth", "B. .py", "C. .p", "D. .python"],
        "answer": "B"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["A. tuple", "B. list", "C. string", "D. int"],
        "answer": "B"
    },
    {
        "question": "How do you create a function in Python?",
        "options": ["A. function myFunction[]", "B. def myFunction():", "C. myFunction(){}", "D. create myFunction()"],
        "answer": "B"
    },
    {
        "question": "What keyword is used to handle exceptions in Python?",
        "options": ["A. catch", "B. try", "C. except", "D. finally"],
        "answer": "B"
    },
    {
        "question": "What does 'len()' do in Python?",
        "options": ["A. Returns the length of an object", "B. Counts the number of elements", "C. Returns the total size", "D. Checks if the object is empty"],
        "answer": "A"
    },
    {
        "question": "Which of the following is a Python framework for web development?",
        "options": ["A. Django", "B. Flask", "C. Both A and B", "D. Ruby on Rails"],
        "answer": "C"
    },
    {
        "question": "What symbol is used for single-line comments in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. --"],
        "answer": "B"
    },
    {
        "question": "What is a lambda function in Python?",
        "options": ["A. Named function", "B. Anonymous function", "C. Standard function", "D. Built-in function"],
        "answer": "B"
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

user_name = input("Enter your name: ")
print(f"Welcome to the Quiz App, {user_name}!")

run_quiz(quiz)
