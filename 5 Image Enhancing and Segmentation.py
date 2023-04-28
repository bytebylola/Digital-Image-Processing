import cv2
import numpy as np

# Load the image
img = cv2.imread(r"ve.webp", cv2.IMREAD_GRAYSCALE)

# Enhance the image using adaptive histogram equalization
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
enhanced = clahe.apply(img)

# Apply Otsu's thresholding to segment the image
_, thresh = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Display the original, enhanced, and segmented images
cv2.imshow('Original Image in Grey-Scale', img)
cv2.imshow('Enhanced Image', enhanced)
cv2.imshow('Segmented Image', thresh)

# Wait for user input to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
