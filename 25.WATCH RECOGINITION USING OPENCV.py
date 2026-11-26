from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Read image
img = cv2.imread("watch.jpg")

# Detect objects
results = model(img)

# Process results
for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        label = model.names[class_id]

        if label == "clock" and confidence > 0.4:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(
                img,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                img,
                f"Watch/Clock: {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

# Save result
cv2.imwrite("watch_detected.jpg", img)

print("Object recognition completed!")
print("Output saved as: watch_detected.jpg")
