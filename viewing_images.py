import cv2
from matplotlib import pyplot as plt

# How each library reads image
# CV2 ==> BGR
# PLT ==> RGB

#  Read image as numpy array
img_bgr = cv2.imread('./Day_1_CV/face.jpg')

# Convert color (from BGR to RGB)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Show in a window
# cv2.imshow("Face", img_rgb)
# cv2.waitKey()  # Prevents window from closing immediately

plt.imshow(img_rgb)
plt.show()
