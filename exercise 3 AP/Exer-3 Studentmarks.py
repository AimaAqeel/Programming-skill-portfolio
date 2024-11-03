# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:28:04 2024

@author: pc
"""

from tkinter import *
from tkinter import messagebox

def load_student_data(filename):
    students = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_students = int(lines[0].strip())
        for line in lines[1:]:
            parts = line.strip().split(',')
            students.append({
                'id': int(parts[0]),
                'name': parts[1],
                'coursework_marks': list(map(int, parts[2:5])),
                'exam_mark': int(parts[5])
            })
    return num_students, students

def calculate_student_data(student):
    total_coursework = sum(student['coursework_marks'])
    total_score = total_coursework + student['exam_mark']
    percentage = (total_score / 160) * 100
    grade = 'A' if percentage >= 70 else 'B' if percentage >= 60 else 'C' if percentage >= 50 \
        else 'D' if percentage >= 40 else 'F'
    return total_coursework, student['exam_mark'], percentage, grade

def view_all_students():
    total_percentage = 0
    result = ""
    for student in students:
        total_coursework, exam_mark, percentage, grade = calculate_student_data(student)
        result += (f"Name: {student['name']}, ID: {student['id']}, Coursework: {total_coursework}, "
                   f"Exam: {exam_mark}, Percentage: {percentage:.2f}%, Grade: {grade}\n")
        total_percentage += percentage
    avg_percentage = total_percentage / len(students)
    result += f"\nClass Summary: Total Students: {len(students)}, Average Percentage: {avg_percentage:.2f}%"
    messagebox.showinfo("All Students", result)

def view_individual_student():
    student_id = int(entry_id.get())
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        total_coursework, exam_mark, percentage, grade = calculate_student_data(student)
        result = (f"Name: {student['name']}, ID: {student['id']}, Coursework: {total_coursework}, "
                  f"Exam: {exam_mark}, Percentage: {percentage:.2f}%, Grade: {grade}")
        messagebox.showinfo("Student Record", result)
    else:
        messagebox.showerror("Error", "Student not found.")

def show_highest_score():
    highest_student = max(students, key=lambda s: sum(s['coursework_marks']) + s['exam_mark'])
    total_coursework, exam_mark, percentage, grade = calculate_student_data(highest_student)
    result = (f"Top Student: {highest_student['name']}, ID: {highest_student['id']}, Coursework: {total_coursework}, "
              f"Exam: {exam_mark}, Percentage: {percentage:.2f}%, Grade: {grade}")
    messagebox.showinfo("Highest Scoring Student", result)

def show_lowest_score():
    lowest_student = min(students, key=lambda s: sum(s['coursework_marks']) + s['exam_mark'])
    total_coursework, exam_mark, percentage, grade = calculate_student_data(lowest_student)
    result = (f"Lowest Scoring Student: {lowest_student['name']}, ID: {lowest_student['id']}, Coursework: {total_coursework}, "
              f"Exam: {exam_mark}, Percentage: {percentage:.2f}%, Grade: {grade}")
    messagebox.showinfo("Lowest Scoring Student", result)

# Load data
filename = "C:\\Users\\pc\\Desktop\\exercise 3 AP\\StudentMarks.txt"
num_students, students = load_student_data(filename)

# GUI setup
root = Tk()
root.title("Student Records")

# Center the window on the screen
window_width, window_height = 400, 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_left = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

# Center the content within the window
Label(root, text="Menu", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=(20, 10))

btn_all_students = Button(root, text="View All Students", command=view_all_students)
btn_all_students.grid(row=1, column=0, columnspan=2, pady=5, padx=20, sticky="ew")

Label(root, text="Enter Student ID:").grid(row=2, column=0, pady=5, padx=(20, 5), sticky="e")
entry_id = Entry(root)
entry_id.grid(row=2, column=1, pady=5, padx=(5, 20), sticky="w")

btn_individual = Button(root, text="View Individual Student", command=view_individual_student)
btn_individual.grid(row=3, column=0, columnspan=2, pady=5, padx=20, sticky="ew")

btn_highest_score = Button(root, text="Show Highest Score", command=show_highest_score)
btn_highest_score.grid(row=4, column=0, columnspan=2, pady=5, padx=20, sticky="ew")

btn_lowest_score = Button(root, text="Show Lowest Score", command=show_lowest_score)
btn_lowest_score.grid(row=5, column=0, columnspan=2, pady=5, padx=20, sticky="ew")

btn_exit = Button(root, text="Exit", command=root.quit)
btn_exit.grid(row=6, column=0, columnspan=2, pady=(10, 20), padx=20, sticky="ew")

root.mainloop()
