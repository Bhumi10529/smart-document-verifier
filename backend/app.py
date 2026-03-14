
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from extractor import extract_fields
from ocr import extract_text
from image_compression import compress_image
from verifier import verify_fields
from doc_classifier import detect_document_type
from preprocessing import check_image_quality
from fraud_detection import check_duplicate

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def home():
    return "system is running"

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    

    # compressed_path = os.path.join("processed_" + file.filename) 
    compressed_path = os.path.join(UPLOAD_FOLDER, "processed_" + file.filename)

    compression_result = compress_image(filepath, compressed_path)
    duplicate_check = check_duplicate(compressed_path)

    quality = check_image_quality(compressed_path)

    # OCR text extraction
    text = extract_text(compressed_path)
    doc_type = detect_document_type(text)

    # Extract important fields
    fields = extract_fields(text)

    # Verify document
    verification = verify_fields(fields)


    result = {
        "document_type": doc_type,
        "duplicate_check": duplicate_check,
        "image_quality": quality,
        "extracted_text": text,
        "fields": fields,
        "compression": compression_result,
        "verification": verification
    }


    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
