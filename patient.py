class PatientManager:
    def retrieve_patient(self, patient_id):
        return f"Details for patient ID: {patient_id} (Mocked data)"

    def add_patient(self, patient_id):
        return f"Patient {patient_id} added successfully. (Mocked)"

    def remove_patient(self, patient_id):
        return f"Patient {patient_id} removed successfully. (Mocked)"
