import cv2
import numpy as np

# Read the image
img = cv2.imread("sample.jpg")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a 5 x 5 kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Black Hat operation
black_hat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

# Save the images
cv2.imwrite("original_gray.jpg", gray)
cv2.imwrite("black_hat_image.jpg", black_hat)

print("Black Hat operation completed successfully!")
print("Original image saved as: original_gray.jpg")
print("Black Hat image saved as: black_hat_image.jpg")
