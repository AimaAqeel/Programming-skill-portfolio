# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 03:50:19 2024

@author: pc
"""

from tkinter import *
import random
from tkinter import messagebox

# Function to display difficulty menu
def displayMenu():
    menu_frame.pack()
    question_frame.pack_forget()
    result_frame.pack_forget()

# Function to generate random integers based on difficulty level
def randomInt(level):
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(1000, 9999)

# Function to decide whether the operation is addition, subtraction, multiplication, or division
def decideOperation():
    return random.choice(['+', '-', '*', '/'])

# Function to display the problem and get the user's answer
def displayProblem():
    global first_num, second_num, operation, attempts
    first_num = randomInt(difficulty)
    second_num = randomInt(difficulty)
    operation = decideOperation()
    attempts = 0
    
    # Ensure division questions have an integer answer
    if operation == '/':
        while first_num % second_num != 0:  # Find numbers that divide evenly
            first_num = randomInt(difficulty)
            second_num = randomInt(difficulty)
    
    question_label.config(text=f"{first_num} {operation} {second_num} = ?")
    answer_entry.delete(0, END)
    question_frame.pack()

# Function to check if the user's answer is correct
def isCorrect(user_answer):
    if operation == '+':
        correct_answer = first_num + second_num
    elif operation == '-':
        correct_answer = first_num - second_num
    elif operation == '*':
        correct_answer = first_num * second_num
    elif operation == '/':
        correct_answer = first_num // second_num  # Integer division for exact results
    
    return user_answer == correct_answer

# Function to handle user's answer submission
def submitAnswer():
    global score, attempts, question_count
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return
    
    if isCorrect(user_answer):
        points = 10 if attempts == 0 else 5
        score += points
        feedback_label.config(text="Correct!", fg="green")
    else:
        attempts += 1
        if attempts < 2:
            feedback_label.config(text="Try again!", fg="orange")
            return
        feedback_label.config(text="Incorrect. Moving to next question.", fg="red")
    
    question_count += 1
    if question_count < 10:
        displayProblem()
    else:
        displayResults()

# Function to display the final results
def displayResults():
    grade = "A+" if score >= 90 else "A" if score >= 80 else "B" if score >= 70 else "C" if score >= 60 else "D" if score >= 50 else "F"
    result_label.config(text=f"Score: {score}/100\nGrade: {grade}")
    menu_frame.pack_forget()
    question_frame.pack_forget()
    result_frame.pack()

# Function to start the quiz
def startQuiz(level):
    global difficulty, score, question_count
    difficulty = level
    score = 0
    question_count = 0
    displayProblem()

# Function to reset the game
def resetGame():
    displayMenu()

# Initialize main window
app = Tk()
app.title("Math Quiz")
app.geometry("300x300")

# Initialize variables
difficulty = 1
score = 0
question_count = 0
first_num, second_num, operation = 0, 0, ''
attempts = 0

# Menu Frame
menu_frame = Frame(app)
menu_label = Label(menu_frame, text="Select Difficulty Level", font=("Arial", 16))
menu_label.pack(pady=10)
easy_button = Button(menu_frame, text="Easy", command=lambda: startQuiz(1))
moderate_button = Button(menu_frame, text="Moderate", command=lambda: startQuiz(2))
advanced_button = Button(menu_frame, text="Advanced", command=lambda: startQuiz(3))
easy_button.pack(fill="x", pady=5)
moderate_button.pack(fill="x", pady=5)
advanced_button.pack(fill="x", pady=5)

# Question Frame
question_frame = Frame(app)
question_label = Label(question_frame, text="", font=("Arial", 16))
question_label.pack(pady=10)
answer_entry = Entry(question_frame)
answer_entry.pack(pady=5)
submit_button = Button(question_frame, text="Submit", command=submitAnswer)
submit_button.pack(pady=5)
feedback_label = Label(question_frame, text="", font=("Arial", 12))
feedback_label.pack(pady=5)

# Result Frame
result_frame = Frame(app)
result_label = Label(result_frame, text="", font=("Arial", 16))
result_label.pack(pady=10)
play_again_button = Button(result_frame, text="Play Again", command=resetGame)
play_again_button.pack(pady=5)

# Start the application
displayMenu()
app.mainloop()

