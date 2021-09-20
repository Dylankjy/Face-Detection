import streamlit as st
import cv2
import numpy as np
from PIL import Image

# UI elements (Text)
st.header("Face detection")
st.text("Provide an image and we'll detect the faces")

# Read classification model from xml
cls = cv2.CascadeClassifier("./Day_1_CV/haarcascade_frontalface_default.xml")


# Detection function
def detect(PIL_img):
    # Convert images in the proper color formats
    cv2_img = cv2.cvtColor(np.array(PIL_img), cv2.COLOR_RGB2BGR)
    cv2_img_bw = cv2.cvtColor(np.array(PIL_img), cv2.COLOR_BGR2GRAY)

    # Bounding boxes
    boxes = cls.detectMultiScale(cv2_img_bw, 1.3, 5)

    for box in boxes:
        # Unpack list values of box
        x, y, width, height = box

        # image, first point, second point, color of box, thickness of line
        cv2.rectangle(cv2_img, (x, y), (x + width, y + height), (0, 255, 0), 2)

    # Render image in frontend
    st.image(cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB))
    st.markdown(f"Detected {len(boxes)} faces")


# UI elements (uploader)
uploaded_file = st.file_uploader("Choose an image to detect", type=['jpeg', 'jpg', 'png'])

# Only run the detection function if uploaded_file is present.
# When loading the page for the first time, this is usually empty.
if uploaded_file is not None:
    PIL_img = Image.open(uploaded_file)
    detect(PIL_img)
