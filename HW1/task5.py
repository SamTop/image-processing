import cv2
import numpy as np
from data import files  # Assuming 'files' contains the list of filenames to process

def apply_thresholds(filenum, hue_thresh=(6, 33), sat_thresh=(80, 175), val_thresh=(71, 176), sv_thresh=(22, 125)):
    input_file = f'images/{filenum}.jpg'
    output_file = f'results/{filenum}.jpg'
    
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

    # Apply thresholds
    mask = np.zeros_like(h, dtype=np.uint8)
    mask[(h >= hue_thresh[0]) & (h <= hue_thresh[1]) &
         (s >= sat_thresh[0]) & (s <= sat_thresh[1]) &
         (v >= val_thresh[0]) & (v <= val_thresh[1]) &
         (sv >= sv_thresh[0]) & (sv <= sv_thresh[1])] = 255

    # Create result image
    # result = np.zeros_like(img)
    img[mask == 0] = [255, 255, 255]  # Set non-complying pixels to white

    # Save the resulting image
    cv2.imwrite(output_file, img)

    print(f"Filtered image saved successfully for {filenum}.")

def main():
    for file in files:
        apply_thresholds(file)
    # apply_thresholds(files[0])

if __name__ == "__main__":
    main()