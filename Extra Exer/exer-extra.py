# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:35:46 2024

@author: pc
"""

from tkinter import *
from tkinter import messagebox, simpledialog

# Initialize an empty list to store student data
students = []

# Calculate student stats
def calculate_student_data(student):
    total = sum(student['coursework_marks']) + student['exam_mark']
    percentage = (total / 160) * 100
    grade = 'A' if percentage >= 70 else 'B' if percentage >= 60 else 'C' if percentage >= 50 else 'D' if percentage >= 40 else 'F'
    return total, percentage, grade

# View all students
def view_all_students():
    result = ""
    for student in students:
        total, percentage, grade = calculate_student_data(student)
        result += f"ID: {student['id']}, Name: {student['name']}, Total: {total}, Percentage: {percentage:.2f}%, Grade: {grade}\n"
    messagebox.showinfo("All Students", result)

# View individual student
def view_individual_student():
    student_id = simpledialog.askinteger("Input", "Enter student ID:")
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        total, percentage, grade = calculate_student_data(student)
        messagebox.showinfo("Student Record", f"ID: {student['id']}, Name: {student['name']}, Total: {total}, Percentage: {percentage:.2f}%, Grade: {grade}")
    else:
        messagebox.showerror("Error", "Student not found.")

# Show highest scoring student
def show_highest_score():
    if students:
        highest_student = max(students, key=lambda s: sum(s['coursework_marks']) + s['exam_mark'])
        total, percentage, grade = calculate_student_data(highest_student)
        messagebox.showinfo("Top Student", f"ID: {highest_student['id']}, Name: {highest_student['name']}, Total: {total}, Percentage: {percentage:.2f}%, Grade: {grade}")
    else:
        messagebox.showinfo("Error", "No students in the records.")

# Show lowest scoring student
def show_lowest_score():
    if students:
        lowest_student = min(students, key=lambda s: sum(s['coursework_marks']) + s['exam_mark'])
        total, percentage, grade = calculate_student_data(lowest_student)
        messagebox.showinfo("Lowest Student", f"ID: {lowest_student['id']}, Name: {lowest_student['name']}, Total: {total}, Percentage: {percentage:.2f}%, Grade: {grade}")
    else:
        messagebox.showinfo("Error", "No students in the records.")

# Sort students
def sort_student_records():
    sort_order = simpledialog.askinteger("Sort Order", "Enter 1 for Ascending or 2 for Descending:")
    sorted_students = sorted(students, key=lambda s: sum(s['coursework_marks']) + s['exam_mark'], reverse=(sort_order == 2))
    result = ""
    for student in sorted_students:
        total, percentage, grade = calculate_student_data(student)
        result += f"ID: {student['id']}, Name: {student['name']}, Total: {total}, Percentage: {percentage:.2f}%, Grade: {grade}\n"
    messagebox.showinfo("Sorted Students", result)

# Add a new student
def add_student_record():
    student_id = simpledialog.askinteger("Input", "Enter student ID:")
    name = simpledialog.askstring("Input", "Enter student name:")
    coursework_marks = [simpledialog.askinteger("Input", f"Enter coursework mark {i+1}:") for i in range(3)]
    exam_mark = simpledialog.askinteger("Input", "Enter exam mark:")
    
    student = {'id': student_id, 'name': name, 'coursework_marks': coursework_marks, 'exam_mark': exam_mark}
    students.append(student)
    messagebox.showinfo("Success", "Student added successfully.")

# Delete a student
def delete_student_record():
    student_id = simpledialog.askinteger("Input", "Enter student ID to delete:")
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        students.remove(student)
        messagebox.showinfo("Success", "Student deleted successfully.")
    else:
        messagebox.showerror("Error", "Student not found.")

# Update student record
def update_student_record():
    student_id = simpledialog.askinteger("Input", "Enter student ID to update:")
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        update_choice = simpledialog.askinteger("Update", "1. Update Coursework\n2. Update Exam Mark\nChoose:")
        if update_choice == 1:
            student['coursework_marks'] = [simpledialog.askinteger("Input", f"Enter new mark {i+1}:") for i in range(3)]
        elif update_choice == 2:
            student['exam_mark'] = simpledialog.askinteger("Input", "Enter new exam mark:")
        messagebox.showinfo("Success", "Student updated successfully.")
    else:
        messagebox.showerror("Error", "Student not found.")

# GUI setup
root = Tk()
root.title("Student Records Management")

# Create buttons for each function
btn_view_all = Button(root, text="View All Students", command=view_all_students)
btn_view_all.pack(pady=5)

btn_view_individual = Button(root, text="View Individual Student", command=view_individual_student)
btn_view_individual.pack(pady=5)

btn_highest_score = Button(root, text="Show Highest Scoring Student", command=show_highest_score)
btn_highest_score.pack(pady=5)

btn_lowest_score = Button(root, text="Show Lowest Scoring Student", command=show_lowest_score)
btn_lowest_score.pack(pady=5)

btn_sort_records = Button(root, text="Sort Student Records", command=sort_student_records)
btn_sort_records.pack(pady=5)

btn_add_student = Button(root, text="Add Student", command=add_student_record)
btn_add_student.pack(pady=5)

btn_delete_student = Button(root, text="Delete Student", command=delete_student_record)
btn_delete_student.pack(pady=5)

btn_update_student = Button(root, text="Update Student Record", command=update_student_record)
btn_update_student.pack(pady=5)

btn_exit = Button(root, text="Exit", command=root.quit)
btn_exit.pack(pady=10)

root.mainloop()
