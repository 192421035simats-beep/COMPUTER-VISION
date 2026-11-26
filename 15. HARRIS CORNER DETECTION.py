import cv2
import numpy as np

# Read the image
img = cv2.imread("sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Apply Harris Corner Detection
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate the detected corners
corners = cv2.dilate(corners, None)

# Mark corners in red
img[corners > 0.01 * corners.max()] = [0, 0, 255]

# Display the result
cv2.imshow("Harris Corner Detection", img)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
