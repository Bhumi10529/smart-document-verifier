from PIL import Image
import os

def compress_image(input_path, output_path, quality=60):
    
    img = Image.open(input_path)

# Convert to RGB if needed
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    img.save(output_path, "JPEG", optimize=True, quality=quality)

    original_size = os.path.getsize(input_path) / 1024
    compressed_size = os.path.getsize(output_path) / 1024

    return {
         "original_size_kb": round(original_size,2),
         "compressed_size_kb": round(compressed_size,2)
    }

