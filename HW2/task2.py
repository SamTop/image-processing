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

    mask_path = f"mask/{filename}.png"
    mask_image = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        raise ValueError("Image not found at the specified path.")
    
    if mask_image is None:
        raise ValueError("Mask image not found at the specified path.")

    # (thresh, im_bw) = cv2.threshold(mask_image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    thresh = 127
    im_bw = cv2.threshold(mask_image, thresh, 255, cv2.THRESH_BINARY)[1]

    # Perform the logical AND operation
    output_image = np.zeros_like(image)
    output_image[im_bw > 0] = image[im_bw > 0]

    # image = cv2.bitwise_and(image, image, mask=im_bw)

    # Save or display the results
    cv2.imwrite(f"face/{filename}.png", output_image)

main()