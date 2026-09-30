import tkinter as tk
from tkinter import font

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Attendance System")
        self.root.geometry("520x460")
        self.root.configure(bg="#f4f6f9")

        self.students = [
            {"id": 1, "name": "Alice Smith", "status": None},
            {"id": 2, "name": "Bob Jones", "status": None},
            {"id": 3, "name": "Charlie Brown", "status": None},
            {"id": 4, "name": "Diana Prince", "status": None},
            {"id": 5, "name": "Evan Wright", "status": None}
        ]

        self.setup_ui()

    def setup_ui(self):
        # Title
        title_font = font.Font(family="Helvetica", size=18, weight="bold")
        title_label = tk.Label(
            self.root,
            text="Student Attendance System",
            font=title_font,
            bg="#f4f6f9",
            fg="#1e293b"
        )
        title_label.pack(pady=(20, 15))

        # Summary Frame
        summary_frame = tk.Frame(self.root, bg="#f4f6f9")
        summary_frame.pack(fill="x", padx=30, pady=(0, 20))

        # Present Card
        present_card = tk.Frame(summary_frame, bg="#f0fdf4", highlightbackground="#bbf7d0", highlightthickness=1, bd=0)
        present_card.pack(side="left", expand=True, fill="both", padx=(0, 6), ipady=10)

        card_title_font = font.Font(family="Helvetica", size=10, weight="bold")
        count_font = font.Font(family="Helvetica", size=22, weight="bold")

        tk.Label(present_card, text="PRESENT", font=card_title_font, bg="#f0fdf4", fg="#166534").pack()
        self.present_count_var = tk.StringVar(value="0")
        tk.Label(present_card, textvariable=self.present_count_var, font=count_font, bg="#f0fdf4", fg="#166534").pack()

        # Absent Card
        absent_card = tk.Frame(summary_frame, bg="#fef2f2", highlightbackground="#fecaca", highlightthickness=1, bd=0)
        absent_card.pack(side="right", expand=True, fill="both", padx=(6, 0), ipady=10)

        tk.Label(absent_card, text="ABSENT", font=card_title_font, bg="#fef2f2", fg="#991b1b").pack()
        self.absent_count_var = tk.StringVar(value="0")
        tk.Label(absent_card, textvariable=self.absent_count_var, font=count_font, bg="#fef2f2", fg="#991b1b").pack()

        # Student List Container
        list_frame = tk.Frame(self.root, bg="#ffffff", highlightbackground="#e2e8f0", highlightthickness=1)
        list_frame.pack(fill="both", expand=True, padx=30, pady=(0, 20))

        name_font = font.Font(family="Helvetica", size=11, weight="bold")
        btn_font = font.Font(family="Helvetica", size=10, weight="bold")

        self.student_rows = []

        for student in self.students:
            row = tk.Frame(list_frame, bg="#ffffff", highlightbackground="#e2e8f0", highlightthickness=1)
            row.pack(fill="x", padx=12, pady=6)

            lbl = tk.Label(row, text=student["name"], font=name_font, bg="#ffffff", fg="#334155")
            lbl.pack(side="left", padx=12, pady=10)

            btn_frame = tk.Frame(row, bg="#ffffff")
            btn_frame.pack(side="right", padx=12)

            p_btn = tk.Button(
                btn_frame,
                text="Present",
                font=btn_font,
                bg="#ffffff",
                fg="#16a34a",
                activebackground="#16a34a",
                activeforeground="#ffffff",
                bd=1,
                relief="solid",
                width=8,
                cursor="hand2",
                command=lambda s_id=student["id"]: self.mark_attendance(s_id, "present")
            )
            p_btn.pack(side="left", padx=4)

            a_btn = tk.Button(
                btn_frame,
                text="Absent",
                font=btn_font,
                bg="#ffffff",
                fg="#dc2626",
                activebackground="#dc2626",
                activeforeground="#ffffff",
                bd=1,
                relief="solid",
                width=8,
                cursor="hand2",
                command=lambda s_id=student["id"]: self.mark_attendance(s_id, "absent")
            )
            a_btn.pack(side="left", padx=4)

            self.student_rows.append({
                "id": student["id"],
                "present_btn": p_btn,
                "absent_btn": a_btn
            })

    def mark_attendance(self, student_id, status):
        for student in self.students:
            if student["id"] == student_id:
                student["status"] = status
                break

        self.update_ui()

    def update_ui(self):
        present_count = sum(1 for s in self.students if s["status"] == "present")
        absent_count = sum(1 for s in self.students if s["status"] == "absent")

        self.present_count_var.set(str(present_count))
        self.absent_count_var.set(str(absent_count))

        for row in self.student_rows:
            student = next(s for s in self.students if s["id"] == row["id"])
            if student["status"] == "present":
                row["present_btn"].configure(bg="#16a34a", fg="#ffffff")
                row["absent_btn"].configure(bg="#ffffff", fg="#dc2626")
            elif student["status"] == "absent":
                row["present_btn"].configure(bg="#ffffff", fg="#16a34a")
                row["absent_btn"].configure(bg="#dc2626", fg="#ffffff")
            else:
                row["present_btn"].configure(bg="#ffffff", fg="#16a34a")
                row["absent_btn"].configure(bg="#ffffff", fg="#dc2626")

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
