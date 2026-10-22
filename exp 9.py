
import cv2
import numpy as np

img = cv2.imread("sample.jpg")

if img is None:
    print("Image not found")
else:
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    h, w = img.shape[:2]
    rotated = cv2.resize(rotated, (w, h))

    result = np.hstack((img, rotated))
    cv2.imshow("Original | Rotated 90 Clockwise", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




