# src/ui_app.py

import tkinter as tk
from tkinter import messagebox
import csv
import datetime
import os

from user import User, authenticate_user
from patient_manager import PatientManager
from stats_manager import StatsManager
from note_manager import NoteManager

class ClinicalApp:
    def __init__(self, master):
        self.master = master
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.user = None

        self.patient_manager = PatientManager("data/Patient_data.csv")
        self.stats_manager = StatsManager("data/Patient_data.csv")
        self.note_manager = NoteManager("data/Patient_data.csv", "data/Notes.csv")

        self.build_login_screen()

    def build_login_screen(self):
        self.clear_window()
        tk.Label(self.master, text="Username").pack(pady=5)
        tk.Entry(self.master, textvariable=self.username_var).pack(pady=5)

        tk.Label(self.master, text="Password").pack(pady=5)
        tk.Entry(self.master, textvariable=self.password_var, show="*").pack(pady=5)

        tk.Button(self.master, text="Login", command=self.login).pack(pady=20)

    def login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        self.user = authenticate_user(username, password, "data/Credentials.csv")

        if self.user:
            self.log_usage(username, self.user.role, "login_success")
            self.build_menu_screen()
        else:
            self.log_usage(username, "unknown", "login_failed")
            messagebox.showerror("Login Failed", "Invalid username or password")

    def build_menu_screen(self):
        self.clear_window()
        tk.Label(self.master, text=f"Welcome, {self.user.username} ({self.user.role})", font=("Arial", 14)).pack(pady=10)

        buttons = {
            "Retrieve Patient": self.patient_manager.retrieve_patient,
            "Add Patient": self.patient_manager.add_patient,
            "Remove Patient": self.patient_manager.remove_patient,
            "Count Visits": self.stats_manager.count_visits,
            "View Note": self.note_manager.view_note,
            "Generate Statistics": self.stats_manager.generate_statistics,
            "Exit": self.master.quit
        }

        allowed = {
            "clinician": ["Retrieve Patient", "Add Patient", "Remove Patient", "Count Visits", "View Note", "Exit"],
            "nurse": ["Retrieve Patient", "Add Patient", "Remove Patient", "Count Visits", "View Note", "Exit"],
            "admin": ["Count Visits", "Exit"],
            "management": ["Generate Statistics", "Exit"]
        }

        for label in allowed.get(self.user.role, []):
            tk.Button(self.master, text=label, width=30, command=buttons[label]).pack(pady=5)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def log_usage(self, username, role, action):
        os.makedirs("output", exist_ok=True)
        log_entry = {
            "username": username,
            "role": role,
            "action": action,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        log_path = "output/usage_log.csv"
        file_exists = os.path.exists(log_path)

        with open(log_path, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=log_entry.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(log_entry)
