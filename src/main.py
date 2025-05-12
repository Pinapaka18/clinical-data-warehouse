# src/main.py

import tkinter as tk
from ui_app import ClinicalApp

def main():
    root = tk.Tk()
    root.title("Clinical Data Warehouse Login")
    root.geometry("600x400")
    app = ClinicalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
