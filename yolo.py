from ultralytics import YOLO
import cv2
import os

model = YOLO("yolov8n.pt")

video_path = "traffic.mp4"

if not os.path.exists(video_path):
    print("Video not found!")
    exit()

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Cannot open video!")
    exit()

cv2.namedWindow("YOLO", cv2.WINDOW_NORMAL)
cv2.resizeWindow("YOLO", 1280, 720)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)
    result = results[0]

    for box in result.boxes:

        class_id = int(box.cls[0])
        class_name = model.names[class_id]
        confidence = float(box.conf[0])

        if confidence < 0.5:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        label = f"{class_name} {confidence:.2f}"

        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    frame = cv2.resize(frame, (1280, 720))

    cv2.imshow("YOLO", frame)

    key = cv2.waitKey(1) & 0xFF

    # Press S to save screenshot
    if key == ord("s"):
        cv2.imwrite("screenshot.jpg", frame)
        print("Screenshot saved as screenshot.jpg")

    # Press Q to quit
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
