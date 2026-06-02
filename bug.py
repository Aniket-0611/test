from ultralytics import YOLO
import cv2

# 1.
#  vehicle_count = 15
# green_time = 10 + vehiclecount * 2
# print('Green time:', green_time)

# Error: NameError: name 'vehiclecount' is not defined

# Corrected code: 1
vehicle_count = 15
green_time = 10 + vehicle_count * 2
print('Green time:', green_time)

# 2.
# signal_state = 'GREEN'
# if signal_state = 'GREEN':
#  print('Gaadiyaan chal sakti hain!')
# else:
#  print('Ruko!')

# Error: SyntaxError: invalid syntax

# Corrected code: 2
signal_state = 'GREEN'
if signal_state == 'GREEN':
    print('Gaadiyaan chal sakti hain!')
else:
    print('Ruko!')

# 3.
# lanes = ['North', 'South', 'East', 'West']
# for lane in lanes
#  print('Lane:', lane)

# Error: SyntaxError: invalid syntax

# Corrected code: 3
lanes = ['North', 'South', 'East', 'West']
for lane in lanes:
    print('Lane:', lane)

# 4.
# import cv2
# img = cv2.imread('traffic.jpg')
# cv2.imshow('Traffic', img)
# cv2.destroyAllWindows()

# Window open hoti hai aur turant band ho jaati hai!

# Corrected code: 4
# import cv2

# img = cv2.imread("traffic.jpg")
# cv2.imshow("Traffic", img)

# cv2.waitKey(0)

# cv2.destroyAllWindows()

# 5.
# model = YOLO('yolov8n.pt')
# img = cv2.imread('traffic.jpg')
# results = model(img)
# for box in results.boxes: # <-- yahan dhyan do
#  class_id = int(box.cls[0])
#  print(model.names[class_id])

# Error: AttributeError: 'Results' object has no attribute 'boxes'

# Corrected code: 5


model = YOLO("yolov8n.pt")
img = cv2.imread("traffic.jpg")

results = model(img)

for box in results[0].boxes:
    class_id = int(box.cls[0])
    print(model.names[class_id])
