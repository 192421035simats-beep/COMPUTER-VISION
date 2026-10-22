
import cv2

cap = cv2.VideoCapture("sample.mp4")

if not cap.isOpened():
    print("Video not found")
else:
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 30

    print("1. Normal")
    print("2. Slow Motion")
    print("3. Fast Motion")
    choice = int(input("Enter choice: "))

    if choice == 1:
        delay = int(1000 / fps)
    elif choice == 2:
        delay = int(2000 / fps)
    elif choice == 3:
        delay = int(500 / fps)
    else:
        print("Invalid choice")
        cap.release()
        raise SystemExit

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(max(1, delay)) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


