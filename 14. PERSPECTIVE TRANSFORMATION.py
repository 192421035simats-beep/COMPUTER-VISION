import cv2
import numpy as np

# Read the image
img = cv2.imread("sample.jpg")

# Get image dimensions
rows, cols = img.shape[:2]

# Source points
pts1 = np.float32([[50, 50], [250, 50], [50, 250], [250, 250]])

# Destination points
pts2 = np.float32([[10, 100], [220, 50], [100, 250], [250, 220]])

# Compute Perspective Transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply Perspective Transformation
result = cv2.warpPerspective(img, matrix, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformed Image", result)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
