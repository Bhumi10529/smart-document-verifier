import cv2

def check_image_quality(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur detection using Laplacian variance
    blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()

    if blur_score > 100:
        quality = "Good"
    elif blur_score > 50:
        quality = "Moderate"
    else:
        quality = "Blurry"

    return {
        "blur_score": round(blur_score,2),
        "quality": quality
    }