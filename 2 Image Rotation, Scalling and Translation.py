import cv2
import numpy as np

# Load the image
img = cv2.imread(r"ve.webp")

# Get the height and width of the image
height, width = img.shape[:2]

# Set the rotation angle in degrees
angle = 45

# Set the scaling factor
scale = 0.5

# Set the translation values
tx = 100
ty = 50

# Define the rotation matrix
M = cv2.getRotationMatrix2D((width/2, height/2), angle, scale)

# Define the translation matrix
T = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply the rotation and translation to the image
rotated_img = cv2.warpAffine(img, M, (width, height))
translated_img = cv2.warpAffine(rotated_img, T, (width, height))

# Display the original and transformed images
cv2.imshow('Original Image', img)
cv2.imshow('Transformed Image', translated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
