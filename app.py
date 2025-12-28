import streamlit as st
import cv2
import numpy as np

from ai_engine.face_detection import detect_face_and_eyes
from ai_engine.overlay import compute_glasses_position, overlay_glasses

st.title("AI Image-Based Eyewear Try-On")

face_file = st.file_uploader("Upload face image", ["jpg", "png"])
glasses_file = st.file_uploader("Upload glasses PNG", ["png"])

if face_file and glasses_file and st.button("Try On"):

    face_img = cv2.imdecode(
        np.frombuffer(face_file.read(), np.uint8),
        cv2.IMREAD_COLOR
    )

    glasses_img = cv2.imdecode(
        np.frombuffer(glasses_file.read(), np.uint8),
        cv2.IMREAD_UNCHANGED
    )

    result = detect_face_and_eyes(face_img)

    if result is None:
        st.error("Face / eyes not detected")
    else:
        left_eye, right_eye, face_box = result

        x, y, gw, gh = compute_glasses_position(
            left_eye, right_eye, face_box, glasses_img
        )

        output = overlay_glasses(face_img.copy(), glasses_img, x, y, gw, gh)

        st.image(
            cv2.cvtColor(output, cv2.COLOR_BGR2RGB),
            use_container_width=True
        )
