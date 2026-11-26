import cv2

# Read the image
img = cv2.imread("sample.jpg")

# Rotate the image by 270 degrees clockwise
rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display the original image
cv2.imshow("Original Image", img)

# Display the rotated image
cv2.imshow("270 Degree Rotated Image", rotated)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
