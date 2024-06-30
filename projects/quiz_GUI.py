import random
import threading
import time
import tkinter as tk
from tkinter import messagebox

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

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        
        self.score = 0
        self.current_question = 0
        random.shuffle(quiz)
        
        self.user_name = tk.StringVar()
        self.answer = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Enter your name:").pack()
        tk.Entry(self.root, textvariable=self.user_name).pack()
        tk.Button(self.root, text="Start Quiz", command=self.start_quiz).pack()
    
    def start_quiz(self):
        self.user_name.set(self.user_name.get().strip())
        if not self.user_name.get():
            messagebox.showerror("Error", "Please enter your name")
            return
        
        self.score = 0
        self.current_question = 0
        self.answer.set("")
        
        self.clear_widgets()
        self.show_question()
    
    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_question(self):
        if self.current_question < len(quiz):
            question = quiz[self.current_question]
            tk.Label(self.root, text=question["question"]).pack()
            for option in question["options"]:
                tk.Radiobutton(self.root, text=option, variable=self.answer, value=option[0]).pack(anchor=tk.W)
            tk.Button(self.root, text="Submit", command=self.submit_answer).pack()
            
            self.time_limit = 10
            self.time_label = tk.Label(self.root, text=f"Time remaining: {self.time_limit} seconds")
            self.time_label.pack()
            self.timer()
        else:
            self.end_quiz()
    
    def timer(self):
        if self.time_limit > 0:
            self.time_limit -= 1
            self.time_label.config(text=f"Time remaining: {self.time_limit} seconds")
            self.root.after(1000, self.timer)
        else:
            self.submit_answer()
    
    def submit_answer(self):
        question = quiz[self.current_question]
        if self.answer.get() == question["answer"]:
            self.score += 1
        
        self.current_question += 1
        self.clear_widgets()
        self.show_question()
    
    def end_quiz(self):
        self.clear_widgets()
        tk.Label(self.root, text=f"You scored {self.score} out of {len(quiz)}").pack()
        
        with open("scores.txt", "a") as f:
            f.write(f"{self.user_name.get()}: {self.score}/{len(quiz)}\n")
        
        tk.Button(self.root, text="Exit", command=self.root.quit).pack()
    
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
