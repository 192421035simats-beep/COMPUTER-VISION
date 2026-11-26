import cv2
import numpy as np

# Read the image
img = cv2.imread("sample.jpg")

# Get image dimensions
rows, cols = img.shape[:2]

# Source points
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Destination points
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Compute Affine Transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply Affine Transformation
result = cv2.warpAffine(img, matrix, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformed Image", result)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
