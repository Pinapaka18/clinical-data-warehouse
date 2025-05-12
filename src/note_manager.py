# src/note_manager.py

import tkinter as tk
from tkinter import simpledialog, messagebox
import pandas as pd
from utils import is_valid_date_format_yyyy_mm_dd

class NoteManager:
    def __init__(self, patient_file, notes_file):
        self.patient_file = patient_file
        self.notes_file = notes_file
        self.load_data()

    def load_data(self):
        try:
            self.df_patients = pd.read_csv(self.patient_file, parse_dates=['Visit_time'])
            self.df_notes = pd.read_csv(self.notes_file)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")
            self.df_patients = pd.DataFrame()
            self.df_notes = pd.DataFrame()

    def view_note(self):
        root = tk.Tk()
        root.withdraw()

        pid = simpledialog.askstring("Patient ID", "Enter Patient ID:")
        date = simpledialog.askstring("Date", "Enter Date (YYYY-MM-DD):")

        if not pid or not date:
            return

        if not is_valid_date_format_yyyy_mm_dd(date):
            messagebox.showerror("Error", "Invalid date format.")
            return

        # Find matching visits
        matched_visits = self.df_patients[
            (self.df_patients['Patient_ID'].astype(str) == pid) &
            (self.df_patients['Visit_time'].dt.strftime('%Y-%m-%d') == date)
        ]

        if matched_visits.empty:
            messagebox.showinfo("Not Found", "No visits found for this patient on the specified date.")
            return

        # Extract note ID and type directly from the patient record
        notes = []
        for _, row in matched_visits.iterrows():
            note_id = row.get("Note_ID", "N/A")
            note_type = row.get("Note_type", "N/A")
            notes.append(f"Note ID: {note_id}\nNote Type: {note_type}\n{'='*40}")

        messagebox.showinfo("Clinical Notes", "\n\n".join(notes))
