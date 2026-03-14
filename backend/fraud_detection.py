import hashlib
import os

HASH_FILE = "document_hashes.txt"

def generate_file_hash(file_path):

    with open(file_path, "rb") as f:
        file_data = f.read()

    return hashlib.md5(file_data).hexdigest()


def check_duplicate(file_path):

    file_hash = generate_file_hash(file_path)

    if not os.path.exists(HASH_FILE):
        open(HASH_FILE, "w").close()

    with open(HASH_FILE, "r") as f:
        hashes = f.read().splitlines()

    if file_hash in hashes:
        return {
            "duplicate": True,
            "message": "Duplicate document detected"
        }

    with open(HASH_FILE, "a") as f:
        f.write(file_hash + "\n")

    return {
        "duplicate": False,
        "message": "Document is unique"
    }