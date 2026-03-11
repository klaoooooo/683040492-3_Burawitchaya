import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # You'll need to install this: pip install tkcalendar
import re

class RegistrationApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Registration")
        self.root.geometry("500x650")
        
        # Variables to store form data
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.program_var = tk.StringVar()
        self.understand_var = tk.BooleanVar(value=False)
        self.dob_var = tk.StringVar()
        self.story_var = ""

        # Start with registration page
        self.current_frame = None
        self.show_registration_page()
        
    def clear_window(self):
        if self.current_frame:
            self.current_frame.destroy()
    
    def show_registration_page(self):
        # Clear all variables
        self.name_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.gender_var.set("Prefer not to say")
        self.program_var.set("Computer Science")
        self.understand_var.set(False)
        self.dob_var.set("")
        self.comment_content = ""  # Clear saved comment content
        
        self.clear_window()
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Title
        ttk.Label(
            self.current_frame,
            text="Student Registration Form",
            font=("Helvetica", 16, "bold")
        ).pack(pady=10)
        
        # Create form fields
        self.create_form_fields()

        # Clear the Text widget after it's created
        self.story_text.delete("1.0", "end")
    
    def create_form_fields(self):
        
        form_frame = ttk.Frame(self.current_frame)
        form_frame.pack(fill='x', pady=5)
        
        # ------------------------
        # Full Name
        ttk.Label(form_frame, text="Full Name:").pack(anchor='w', pady=(10, 0))
        ttk.Entry(form_frame, textvariable=self.name_var, width=50).pack(anchor='w', pady=2, fill='x')
        self.name_var.set("Burawitchaya Rongthong")

        # Email
        ttk.Label(form_frame, text="Email:").pack(anchor='w', pady=(10, 0))
        ttk.Entry(form_frame, textvariable=self.email_var, width=50).pack(anchor='w', pady=2, fill='x')
        self.email_var.set("burawitchaya.r@kkumail.com")

        # Phone
        ttk.Label(form_frame, text="Phone:").pack(anchor='w', pady=(10, 0))
        ttk.Entry(form_frame, textvariable=self.phone_var, width=50).pack(anchor='w', pady=2, fill='x')
        self.phone_var.set("xxxxxxxxxx")
        # ------------------------
               
        # Date of Birth
        # Calendar input
        ttk.Label(form_frame, text="Date of Birth:").pack(anchor='w', pady=(10,0))
        self.dob_entry = DateEntry(
            form_frame,
            width=20,
            background='darkblue',
            foreground='white',
            borderwidth=2,
            day = 11,
            month=3,
            year=2007,
            textvariable=self.dob_var
        )
        self.dob_entry.pack(anchor='w', pady=2)

        # ------------------------
        # Gender
        ttk.Label(form_frame, text="Gender:").pack(anchor='w', pady=(10, 0))
        gender_frame = ttk.Frame(form_frame)
        gender_frame.pack(anchor='w', pady=2)
        for option in ["Male", "Female", "Non-binary", "Prefer not to say"]:
            ttk.Radiobutton(
                gender_frame,
                text=option,
                variable=self.gender_var,
                value=option
            ).pack(side='left', padx=5)
        self.gender_var.set("Male")

        # Program
        ttk.Label(form_frame, text="Program:").pack(anchor='w', pady=(10, 0))
        program_combo = ttk.Combobox(
            form_frame,
            textvariable=self.program_var,
            values=["Computer Science", "Engineering", "Business", "Arts", "Sciences"],
            state="readonly",
            width=47
        )
        self.program_var.set("Engineering")
        program_combo.pack(anchor='w', pady=2, fill='x')

        # Tell us a little bit about yourself
        ttk.Label(form_frame, text="Tell us a little bit about yourself:").pack(anchor='w', pady=(10, 0))
        self.story_text = tk.Text(form_frame, width=50, height=4)  # height = จำนวนบรรทัด
        self.story_text.pack(anchor='w', pady=2, fill='x')
        self.story_text.insert("1.0", "Eating time!")


        # Accept terms checkbox
        ttk.Checkbutton(
            form_frame,
            text="I accept the terms and conditions.",
            variable=self.understand_var
        ).pack(anchor='w', pady=(10, 0))
        self.understand_var.set(True)
        # Submit button
        ttk.Button(
            form_frame,
            text="Submit Registration",
            command=self.validate_and_submit
        ).pack(pady=15)
        # ------------------------
    
    def validate_and_submit(self):
        # Basic validation
        if not self.name_var.get().strip():
            messagebox.showerror("Error", "Please enter your name")
            return
        
        if not self.validate_email(self.email_var.get()):
            messagebox.showerror("Error", "Please enter a valid email address")
            return
        
        if not self.validate_phone(self.phone_var.get()):
            messagebox.showerror("Error", "Please enter a valid phone number")
            return
        
        if not self.understand_var.get():
            messagebox.showerror("Error", "Please accept the terms and conditions.")
            return

        # save text in the comment box
        self.story_content = self.story_text.get("1.0", "end-1c")

        # If validation passes, show confirmation page
        self.show_confirmation_page()
    
    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_phone(self, phone):
        pattern = r'^\d{9,10}$'
        return re.match(pattern, phone) is not None
    
    def show_confirmation_page(self):

        self.clear_window()
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # ------------------------
        # Title
        ttk.Label(
            self.current_frame,
            text="Registration Confirmed!",
            font=("Helvetica", 16, "bold")
        ).pack(pady=15)

        # Info frame for label-value pairs
        info_frame = ttk.Frame(self.current_frame)
        info_frame.pack(fill='x', padx=20, pady=10)

        fields = [
            ("Name:", self.name_var.get()),
            ("Email:", self.email_var.get()),
            ("Phone:", self.phone_var.get()),
            ("Date of Birth:", self.dob_var.get()),
            ("Gender:", self.gender_var.get()),
            ("Program:", self.program_var.get()),
            ("Your story:", self.story_content),
        ]

        for label_text, value_text in fields:
            row = ttk.Frame(info_frame)
            row.pack(fill='x', pady=4)
            ttk.Label(row, text=label_text, font=("Helvetica", 10, "bold"), width=14, anchor='w').pack(side='left')
            ttk.Label(row, text=value_text, anchor='w').pack(side='left')

        # New Registration button
        ttk.Button(
            self.current_frame,
            text="New Registration",
            command=self.show_registration_page
        ).pack(pady=20)
        # ------------------------
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = RegistrationApp()
    app.run()
