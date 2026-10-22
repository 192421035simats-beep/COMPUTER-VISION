import cv2

image = cv2.imread(r"C:\Users\DELL\Documents\computer vision lab\sample.jpeg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray_image, 100, 200)

cv2.imshow("Original Image", image)
cv2.imshow("Edge Detected Image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
