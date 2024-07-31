import cv2
import numpy as np
from data import files

def main():
    # Load the image
    for filename in files:
        processImage(filename)

def processImage(filename):
    image_path = f"images/{filename}.jpg"
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found at the specified path.")

    # Convert BGR (OpenCV's default) to RGB
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert RGB to HSB (Hue, Saturation, Brightness)
    hsv_image = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)

    h, s, v = cv2.split(hsv_image)

    # Compute normalized saturation * brightness (S * V)
    sv = np.uint8(np.clip((s.astype(float) / 255.0) * (v.astype(float) / 255.0) * 255.0, 0, 255))

    # Apply the threshold
    binary_mask = np.zeros_like(h, dtype=np.uint8)
    binary_mask[(h >= 3) & (h <= 24) & (sv >= 40) & (sv <= 80)] = 255


    # Save or display the results
    cv2.imwrite(f"temp/{filename}.jpg", binary_mask)  # Save the image

main()