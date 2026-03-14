import easyocr

reader = easyocr.Reader(['en'])

def extract_text(image_path):

    results = reader.readtext(image_path)

    extracted_text = ""

    for detection in results:
        extracted_text += detection[1] + " "

    return extracted_text