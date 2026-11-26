import cv2

# Read the original image
original = cv2.imread("sample.jpg")

# Read the watermark image
watermark = cv2.imread("watermark.png")

# Check whether images are loaded
if original is None:
    print("Error: Original image not found!")
    exit()

if watermark is None:
    print("Error: Watermark image not found!")
    exit()

# Resize watermark
watermark = cv2.resize(watermark, (200, 100))

# Get watermark dimensions
h, w = watermark.shape[:2]

# Position watermark at bottom-right corner
x = original.shape[1] - w - 20
y = original.shape[0] - h - 20

# Select region of interest
roi = original[y:y+h, x:x+w]

# Blend original region and watermark
result = cv2.addWeighted(roi, 0.7, watermark, 0.3, 0)

# Insert blended watermark
original[y:y+h, x:x+w] = result

# Save the watermarked image
cv2.imwrite("watermarked_image.jpg", original)

print("Watermark inserted successfully!")
print("Output saved as: watermarked_image.jpg")
