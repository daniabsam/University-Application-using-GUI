import tkinter as tk
# Course records list
course_records = []
def submit_course():
    course_data = {}
    course_data["class"] = class_entry.get()
    course_data["date"] = date_entry.get()
    course_data["faculty"] = faculty_entry.get()
    course_records.append(course_data)
    class_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    faculty_entry.delete(0, tk.END)

def show_records():
    records_window = tk.Toplevel(root)
    records_window.title("Course Records")
    records_window.configure(bg="#efcfe3")
    records_frame = tk.Frame(records_window, bg="#fbe7ef", padx=20, pady=20)
    records_label = tk.Label(records_frame, text="Course Records:", bg="#fbe7ef")
    records_label.grid(row=0, column=0)
    records_text = tk.Text(records_frame, height=10, width=50)
    records_text.grid(row=1, column=0)
    for record in course_records:
        records_text.insert(tk.END, f"Class: {record['class']}\nDate: {record['date']}\nFaculty: {record['faculty']}\n\n")
root = tk.Tk()
root.title("Course Management System")
root.configure(bg="#efcfe3")

course_frame = tk.Frame(root, bg="#fbe7ef", padx=20, pady=20)
course_frame.pack()

class_label = tk.Label(course_frame, text="Course:", bg="#fbe7ef")
class_label.grid(row=0, column=0)

class_entry = tk.Entry(course_frame, width=50)
class_entry.grid(row=0, column=1)

date_label = tk.Label(course_frame, text="Date:", bg="#fbe7ef")
date_label.grid(row=1, column=0)

date_entry = tk.Entry(course_frame, width=50)
date_entry.grid(row=1, column=1)

faculty_label = tk.Label(course_frame, text="Faculty:", bg="#fbe7ef")
faculty_label.grid(row=2, column=0)

faculty_entry = tk.Entry(course_frame, width=50)
faculty_entry.grid(row=2, column=1)

submit_button = tk.Button(course_frame, text="Submit", bg="#be5683", fg="white", command=submit_course)
submit_button.grid(row=3, column=0, pady=10)

show_records_button = tk.Button(course_frame, text="Show Records", bg="#be5683", fg="white", command=show_records)
show_records_button.grid(row=3, column=1, pady=10)
root.mainloop()