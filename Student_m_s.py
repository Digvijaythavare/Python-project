import tkinter as tk
from tkinter import messagebox, ttk

# List to store student data
students = []

# Function to add a new student
def add_student():
    student_id = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()

    if not student_id or not name or not age or not grade:
        messagebox.showwarning("Input Error", "All fields are required")
        return

    # Check if student ID already exists
    for student in students:
        if student['id'] == student_id:
            messagebox.showwarning("Duplicate ID", "Student ID already exists")
            return

    student = {"id": student_id, "name": name, "age": age, "grade": grade}
    students.append(student)
    messagebox.showinfo("Success", f"Student {name} added successfully")
    clear_entries()
    view_students()

# Function to view all students in the treeview
def view_students():
    for row in tree.get_children():
        tree.delete(row)
    for student in students:
        tree.insert("", "end", values=(student['id'], student['name'], student['age'], student['grade']))

# Function to select a student from treeview
def select_student(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, 'values')
        entry_id.delete(0, tk.END)
        entry_id.insert(0, values[0])
        entry_name.delete(0, tk.END)
        entry_name.insert(0, values[1])
        entry_age.delete(0, tk.END)
        entry_age.insert(0, values[2])
        entry_grade.delete(0, tk.END)
        entry_grade.insert(0, values[3])

# Function to update selected student
def update_student():
    student_id = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()

    for student in students:
        if student['id'] == student_id:
            student['name'] = name
            student['age'] = age
            student['grade'] = grade
            messagebox.showinfo("Success", f"Student {name} updated successfully")
            view_students()
            clear_entries()
            return
    messagebox.showwarning("Not Found", "Student ID not found")

# Function to delete selected student
def delete_student():
    student_id = entry_id.get()
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            messagebox.showinfo("Deleted", f"Student {student_id} deleted successfully")
            view_students()
            clear_entries()
            return
    messagebox.showwarning("Not Found", "Student ID not found")

# Function to clear entry fields
def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_grade.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x400")

# Labels and Entries
tk.Label(root, text="Student ID").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Name").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Age").grid(row=2, column=0, padx=10, pady=5)
tk.Label(root, text="Grade").grid(row=3, column=0, padx=10, pady=5)

entry_id = tk.Entry(root)
entry_name = tk.Entry(root)
entry_age = tk.Entry(root)
entry_grade = tk.Entry(root)

entry_id.grid(row=0, column=1, padx=10, pady=5)
entry_name.grid(row=1, column=1, padx=10, pady=5)
entry_age.grid(row=2, column=1, padx=10, pady=5)
entry_grade.grid(row=3, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Student", command=add_student).grid(row=4, column=0, pady=10)
tk.Button(root, text="Update Student", command=update_student).grid(row=4, column=1, pady=10)
tk.Button(root, text="Delete Student", command=delete_student).grid(row=4, column=2, pady=10)
tk.Button(root, text="Clear Fields", command=clear_entries).grid(row=4, column=3, pady=10)

# Treeview to display students
columns = ("ID", "Name", "Age", "Grade")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

tree.bind("<<TreeviewSelect>>", select_student)

root.mainloop()