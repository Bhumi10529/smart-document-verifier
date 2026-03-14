def detect_document_type(text):

    text = text.lower()

    if "aadhaar" in text or "uidai" in text:
        return "Aadhaar Card"

    elif "income certificate" in text:
        return "Income Certificate"

    elif "permanent account number" in text or "pan" in text:
        return "PAN Card"

    else:
        return "Unknown Document"