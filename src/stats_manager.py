# src/stats_manager.py

import tkinter as tk
from tkinter import simpledialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from utils import is_valid_date_format_yyyy_mm_dd

class StatsManager:
    def __init__(self, patient_file):
        self.patient_file = patient_file
        self.load_data()

    def load_data(self):
        try:
            self.df = pd.read_csv(self.patient_file, parse_dates=['Visit_time'])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load patient data: {e}")
            self.df = pd.DataFrame()

    def count_visits(self):
        root = tk.Tk()
        root.withdraw()
        date = simpledialog.askstring("Visit Date", "Enter date (YYYY-MM-DD):")

        if not is_valid_date_format_yyyy_mm_dd(date):
            messagebox.showerror("Error", "Invalid date format.")
            return

        visits_on_date = self.df[self.df['Visit_time'].dt.strftime('%Y-%m-%d') == date]
        total = len(visits_on_date)
        unique_patients = visits_on_date['Patient_ID'].nunique()

        messagebox.showinfo(
            "Visit Count",
            f"Date: {date}\nTotal Visits: {total}\nUnique Patients: {unique_patients}"
        )

    def generate_statistics(self):
        if self.df.empty:
            messagebox.showerror("Error", "No data available to generate statistics.")
            return

        try:
            # Plot 1: Visits by Department
            dept_counts = self.df['Visit_department'].value_counts()
            dept_counts.plot(kind='bar', title='Visits by Department')
            plt.xlabel("Department")
            plt.ylabel("Number of Visits")
            plt.tight_layout()
            plt.show()

            # Plot 2: Gender Distribution
            gender_counts = self.df['Gender'].value_counts()
            gender_counts.plot(kind='pie', title='Gender Distribution', autopct='%1.1f%%')
            plt.ylabel('')
            plt.tight_layout()
            plt.show()

            # Plot 3: Age Distribution
            self.df['Age'].dropna().plot(kind='hist', bins=10, title='Age Distribution')
            plt.xlabel("Age")
            plt.ylabel("Frequency")
            plt.tight_layout()
            plt.show()

            messagebox.showinfo("Statistics", "Key statistics displayed successfully.")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate statistics: {e}")
