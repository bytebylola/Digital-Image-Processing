import cv2
import numpy as np

# Load the image
img = cv2.imread(r"ve.webp")

# Define the structuring element for erosion and dilation
kernel = np.ones((2,3), np.uint8)

# Apply erosion to the image
eroded = cv2.erode(img, kernel)

# Subtract the eroded image from the original image
edge = cv2.absdiff(img, eroded)

# Display the original image and edge image
cv2.imshow('Original Image', img)
cv2.imshow('Edge Image with Erosion', edge)

# Apply dilation to the image
dilated = cv2.dilate(img, kernel)

# Subtract the dilated image from the original image
edge2 = cv2.absdiff(img, dilated)

# Display the edge image with dilation
cv2.imshow('Edge Image with Dilation', edge2)

# Wait for user input to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
