import cv2
import numpy as np
from PIL import Image
import streamlit as st

MODEL = "Module_1\\Week_4\\Homework\\model\\MobileNetSSD_deploy.caffemodel"
PROTOTXT = "Module_1\\Week_4\\Homework\\model\\MobileNetSSD_deploy.prototxt.txt"


def process_image(img):
    # Ensure img is a NumPy array
    if not isinstance(img, np.ndarray):
        # If img is a PIL Image, convert to NumPy array
        if isinstance(img, Image.Image):
            img = np.array(img)
        else:
            raise TypeError("img must be a PIL.Image.Image or a numpy.ndarray")

    blob = cv2.dnn.blobFromImage(
        cv2.resize(img, (300, 300)), 0.007483, (300, 300), 127.5
    )
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)
    detections = net.forward()
    return detections


def annotate_image(img, detections, confidence_threshold=0.5):
    # Convert img to a NumPy array if it is a PIL Image
    if isinstance(img, Image.Image):
        img = np.array(img)

    # Loop over detections
    (h, w) = img.shape[:2]
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > confidence_threshold:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (start_x, start_y, end_x, end_y) = box.astype("int")
            cv2.rectangle(img, (start_x, start_y), (end_x, end_y), 70, 2)

    return img


def main():
    st.title("Object dectection for images")
    file = st.file_uploader("Upload image", type=["jpg", "png", "jpeg"])
    if file is not None:
        st.image(file, caption="Uploaded image")
        img = Image.open(file)
        detections = process_image(img)
        processed_image = annotate_image(img, detections)
        st.image(processed_image, caption="Processed image")


if __name__ == '__main__':
    main()
