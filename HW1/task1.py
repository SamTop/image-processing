import cv2
import numpy as np
from data import files  # Assuming 'files' contains the list of filenames to process

def hsb_stack(filenum):
    input_file = f'images/{filenum}.jpg'
    
    # Read the input image
    img = cv2.imread(input_file)

    # Convert BGR (OpenCV's default) to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert RGB to HSB (Hue, Saturation, Brightness)
    img_hsb = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)

    # Split channels
    h, s, v = cv2.split(img_hsb)

    # Compute normalized saturation * brightness (S * V)
    sv = np.uint8(np.clip((s.astype(float) / 255.0) * (v.astype(float) / 255.0) * 255.0, 0, 255))

    # Save each channel as a separate image
    cv2.imwrite(f"hue/{filenum}-0.png", h)
    cv2.imwrite(f"sat/{filenum}-1.png", s)
    cv2.imwrite(f"val/{filenum}-2.png", v)
    cv2.imwrite(f"sv/{filenum}-3.png", sv)  # Save S * V as grayscale image

    print(f"HSB channels saved successfully for {filenum}.")

def main():
    for file in files:
        hsb_stack(file)

if __name__ == "__main__":
    main()
