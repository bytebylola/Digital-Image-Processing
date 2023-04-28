import cv2
import numpy as np

# Load the image
img = cv2.imread(r"ve.webp")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection using the Canny algorithm
edges = cv2.Canny(gray, 100, 200)

# Apply texture extraction using the Laplacian of Gaussian (LoG) filter
gray = cv2.GaussianBlur(gray, (3, 3), 0)
log = cv2.Laplacian(gray, cv2.CV_64F)

# Display the original image and extracted features
cv2.imshow('Original Image', img)
cv2.imshow('Edges', edges)
cv2.imshow('Texture', log)

# Wait for user input to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
