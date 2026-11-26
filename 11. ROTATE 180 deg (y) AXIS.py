import cv2

# Read the image
img = cv2.imread("sample.jpg")

# Rotate the image by 180 degrees
rotated = cv2.rotate(img, cv2.ROTATE_180)

# Display the original image
cv2.imshow("Original Image", img)

# Display the rotated image
cv2.imshow("180 Degree Rotated Image", rotated)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
