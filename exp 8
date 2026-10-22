
import cv2
import numpy as np

img = cv2.imread("sample.jpg")

if img is None:
    print("Image not found")
else:
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(img, kernel, iterations=1)
    result = np.hstack((img, dilated))
    cv2.imshow("Original | Dilated", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


