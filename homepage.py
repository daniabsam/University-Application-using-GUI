import tkinter as tk
root = tk.Tk()
root.title("Home")
root.configure(bg="#efcfe3")
def open_attendance():
    attendance_window = tk.Toplevel(root)
    attendance_window.title("Attendance")
    attendance_window.configure(bg="#efcfe3")
def open_student_records():
    student_records_window = tk.Toplevel(root)
    student_records_window.title("Student Records")
    student_records_window.configure(bg="#efcfe3")
def open_course_management():
    course_management_window = tk.Toplevel(root)
    course_management_window.title("Course Management")
    course_management_window.configure(bg="#efcfe3")
def open_fee_report():
    fee_report_window = tk.Toplevel(root)
    fee_report_window.title("Fee Report")
    fee_report_window.configure(bg="#efcfe3")

attendance_button = tk.Button(root, text="Attendance", bg="#fbe7ef", fg="black", command=open_attendance)
attendance_button.pack(pady=10)
student_records_button = tk.Button(root, text="Student Records", bg="#fbe7ef", fg="black", command=open_student_records)
student_records_button.pack(pady=10)
course_management_button = tk.Button(root, text="Course Management", bg="#fbe7ef", fg="black", command=open_course_management)
course_management_button.pack(pady=10)
fee_report_button = tk.Button(root, text="Fee Report", bg="#fbe7ef", fg="black", command=open_fee_report)
fee_report_button.pack(pady=10)
root.mainloop()