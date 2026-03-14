import re

def extract_fields(text):

    name = None
    dob = None
    aadhaar = None

    # Aadhaar number pattern
    aadhaar_match = re.search(r"\d{4}\s\d{4}\s\d{4}", text)
    if aadhaar_match:
        aadhaar = aadhaar_match.group()

    # Date of birth pattern
    dob_match = re.search(r"\d{2}/\d{2}/\d{4}", text)
    if dob_match:
        dob = dob_match.group()

    # Name (simple assumption: first line with letters)
    words = text.split()
    if len(words) > 1:
        name = words[0] + " " + words[1]

    return {
        "name": name,
        "dob": dob,
        "aadhaar_number": aadhaar
    }