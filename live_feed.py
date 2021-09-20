import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# This will constantly obtain frames from video camera
while True:
    ret, frame = cap.read()
    print(frame)
    cv2.imshow("myCapture", frame)

    # Continue until 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Termination point
        break

