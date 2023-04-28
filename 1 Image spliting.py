import cv2

# Load the image from file
img = cv2.imread(r"ve.webp")

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not read image file")
else:
    # Get the height and width of the image
    height, width, _ = img.shape

    # Split the image into 4 quadrants
    top_left = img[0:height//2, 0:width//2]
    top_right = img[0:height//2, width//2:width]
    bottom_left = img[height//2:height, 0:width//2]
    bottom_right = img[height//2:height, width//2:width]

    # Display the 4 quadrants
    cv2.imshow("Top Left", top_left)
    cv2.imshow("Top Right", top_right)
    cv2.imshow("Bottom Left", bottom_left)
    cv2.imshow("Bottom Right", bottom_right)
    cv2.waitKey(0)

# Clean up
cv2.destroyAllWindows()
