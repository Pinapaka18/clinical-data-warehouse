Clinical Data Warehouse – Final Project (HI 741, Spring 2025)
This is a Python-based GUI application that simulates a clinical data warehouse. Users can securely log in, manage patient records, retrieve clinical notes, and generate useful statistics based on real-time CSV files.

📦 How to Run
✅ Requirements
This program requires Python 3.11+ and the following packages:

pandas

matplotlib

tkinter (included by default in Python)

💻 Install Packages
Using pip:

pip install -r requirements.txt

Or using Anaconda:

conda create -n hi741_project python=3.11

conda activate hi741_project

pip install -r requirements.txt

▶️ Run the Program
Open terminal in the root directory and run:
python src/main.py

📝 Description of the Program
The Clinical Data Warehouse application is a modular, GUI-based health information system designed to simulate real-world clinical record management. It was developed using Python and Tkinter to provide secure, role-based access for hospital staff and support real-time interaction with patient and clinical data stored in CSV files.

🔐 Login & Credential Validation
Users are required to log in with a username and password validated against Credentials.csv. All login attempts (successful or failed) are automatically logged in output/usage_log.csv.

👥 Role-Based Access Control (RBAC)
Role	Features Available
Admin	Count Visits only
Nurse	Add, Remove, Retrieve Patient; Count Visits; View Notes
Clinician	Same as Nurse
Management	Generate Statistics (visit frequency, age distribution, gender/ethnicity breakdown)

🖼 GUI Design with Tkinter
Simple and intuitive layout

Form-based input with pop-up dialogs

Real-time feedback for all actions

Designed for usability by non-technical users

💾 Real-Time Data Updates
Patient_data.csv: Updates immediately after adding/removing a patient

Notes.csv: Read-only data displayed for viewing notes

usage_log.csv: Stores every action performed by users (login, retrieve, add, delete, view)

Project structure :

Final Project/
├── data/
│   ├── Credentials.csv
│   ├── Patient_data.csv
│   └── Notes.csv
├── output/
│   └── usage_log.csv
├── src/
│   ├── main.py
│   ├── ui_app.py
│   ├── user.py
│   ├── patient_manager.py
│   ├── stats_manager.py
│   ├── note_manager.py
│   └── utils.py
└── requirements.txt


📊 Logging & Auditing
Each user interaction is recorded in usage_log.csv including:

Username

Role

Timestamp

Action performed

This ensures full traceability and is essential for compliance in healthcare systems.
