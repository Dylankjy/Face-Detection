import cv2
from matplotlib import pyplot as plt

cls = cv2.CascadeClassifier("./Day_1_CV/haarcascade_frontalface_default.xml")

img = cv2.imread("./Day_1_CV/face.jpg")

# Convert images to greyscale
img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Bounding boxes
boxes = cls.detectMultiScale(img_bw, 1.3, 5)

for box in boxes:
    # Unpack list values of box
    x, y, width, height = box

    # image, first point, second point, color of box, thickness of line
    cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 2)

cv2.imshow("Detection", img)
cv2.waitKey()
