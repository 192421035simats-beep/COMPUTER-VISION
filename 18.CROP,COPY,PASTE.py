import cv2

# Read the source image
img = cv2.imread("sample.jpg")

# Check image
if img is None:
    print("Error: Image not found!")
    exit()

# Select ROI
roi = img[50:138, 50:246]

# Copy the ROI
copied_roi = roi.copy()

# Get ROI dimensions
h, w = copied_roi.shape[:2]

# Get image dimensions
img_h, img_w = img.shape[:2]

# Choose a safe destination position
x = img_w - w - 20
y = img_h - h - 20

# Check if enough space is available
if x < 0 or y < 0:
    print("Error: ROI is too large for the image.")
    exit()

# Paste ROI at bottom-right
img[y:y+h, x:x+w] = copied_roi

# Save cropped ROI
cv2.imwrite("cropped_roi.jpg", copied_roi)

# Save final image
cv2.imwrite("roi_copy_paste.jpg", img)

print("ROI cropped successfully!")
print("ROI copied and pasted successfully!")
print("Output saved as roi_copy_paste.jpg")
