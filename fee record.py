import tkinter as tk
# Student list
students = []
def generate_report():
    name = name_entry.get()
    reg_no = reg_no_entry.get()
    course = course_entry.get()
    fees = fees_entry.get()
    students.append({"name": name, "reg_no": reg_no, "course": course, "fees": fees})

    report_window = tk.Toplevel(root)
    report_window.title("Fee Report")
    report_window.configure(bg="#efcfe3")

    report_frame = tk.Frame(report_window, bg="#fbe7ef", padx=20, pady=20)
    report_frame.pack()

    report_label = tk.Label(report_frame, text="Fee Report:", bg="#fbe7ef")
    report_label.grid(row=0, column=0)

    report_text = tk.Text(report_frame, height=10, width=50)
    report_text.grid(row=1, column=0)

    report_text.insert(tk.END, f"Name: {name}\nReg No: {reg_no}\nCourse: {course}\nFees Paid: {fees}\n\n")

    name_entry.delete(0, tk.END)
    reg_no_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    fees_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Fee Report System")
root.configure(bg="#efcfe3")

input_frame = tk.Frame(root, bg="#fbe7ef", padx=20, pady=20)
input_frame.pack()
# Create labels and entry boxes for input
name_label = tk.Label(input_frame, text="Name:", bg="#fbe7ef")
name_label.grid(row=0, column=0)

name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1)

reg_no_label = tk.Label(input_frame, text="Registration No:", bg="#fbe7ef")
reg_no_label.grid(row=1, column=0)

reg_no_entry = tk.Entry(input_frame)
reg_no_entry.grid(row=1, column=1)

course_label = tk.Label(input_frame, text="Course:", bg="#fbe7ef")
course_label.grid(row=2, column=0)

course_entry = tk.Entry(input_frame)
course_entry.grid(row=2, column=1)

fees_label = tk.Label(input_frame, text="Fees Paid:", bg="#fbe7ef")
fees_label.grid(row=3, column=0)

fees_entry = tk.Entry(input_frame)
fees_entry.grid(row=3, column=1)

generate_report_button = tk.Button(root, text="Generate Report", bg="#be5683", fg="white", command=generate_report)
generate_report_button.pack(pady=10)

root.mainloop()