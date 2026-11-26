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

# Apply erosion
eroded = cv2.erode(gray, kernel, iterations=1)

# Save the images
cv2.imwrite("original_gray.jpg", gray)
cv2.imwrite("eroded_image.jpg", eroded)

print("Erosion operation completed successfully!")
print("Original image saved as: original_gray.jpg")
print("Eroded image saved as: eroded_image.jpg")
