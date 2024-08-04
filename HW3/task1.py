import cv2
import numpy as np

import cv2
import numpy as np
from data1 import files

def main():
    # Load the image
    for filename in files:
        processImage(filename)

def processImage(filename):
    # Read the image in grayscale
    image = cv2.imread(f"../HW2/mask/{filename}.png", cv2.IMREAD_GRAYSCALE)

    # Threshold the image to get a binary image
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Create a structuring element for the closing operation
    radius = 5
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*radius + 1, 2*radius + 1))

    # Perform the closing operation
    closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

    # Find contours of the closed binary image
    contours, _ = cv2.findContours(closed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour
    largest_contour = max(contours, key=cv2.contourArea)

    # Calculate the bounding ellipse for the largest contour
    ellipse = cv2.fitEllipse(largest_contour)

    # Draw the ellipse on the original image
    output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    (center_x, center_y), (width, height), angle = ellipse
    top_left_x = int(center_x - width / 2)
    top_left_y = int(center_y - height / 2)

    print(f"{filename} -- {top_left_x}, {top_left_y}, {format(width, ".2f")}, {format(height, ".2f")}")

main()