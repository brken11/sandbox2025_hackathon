#import pyresseract
from pdf2image import convert_from_path
import json
import re
import typing

def parse_patient_form(text):
    """
    Attempts to parse raw text into json
    """

    data: dict = {}

    patterns = {
            "patient_id" : r"Patient ID:\s*(\d+)",
            "name" : r"Name:\s*([A-Za-z\s]+)",
            "date_of_birth": r"Date of Birth:\s*([\d-]+)",
            "address": r"Address:\s*(.*)",
            "phone": r"Phone:\s*([\d\(\)\- ]+)",
            "email": r"Email:\s*([\w\.-]+@[\w\.-]+\.\w+)",
            "appointment_date": r"Appointment Date:\s*([\d-]+)",
            "doctor" : r"Doctor:\s*([A-Za-z\s]+)",
            "diagnosis": r"Diagnosis:\s*(.*)"
    }

    for key, pat in patterns.items():
        match = re.search(pat, text, re.MULTILINE);
        if match:
            data[key] = match.group(1).strip()

    return data
