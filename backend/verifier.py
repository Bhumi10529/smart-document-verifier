def verify_fields(extracted_fields):

    score = 0
    total = 3

    if extracted_fields.get("name"):
        score += 1

    if extracted_fields.get("dob"):
        score += 1

    if extracted_fields.get("aadhaar_number"):
        score += 1

    confidence = (score / total) * 100

    return {
        "verification_score": confidence,
        "status": "Verified" if confidence >= 60 else "Needs Review"
    }