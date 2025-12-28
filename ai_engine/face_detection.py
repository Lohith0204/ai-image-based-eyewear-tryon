import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

def detect_face_and_eyes(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        return None

    x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
    roi_gray = gray[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)
    if len(eyes) < 2:
        return None

    eyes = sorted(eyes, key=lambda e: e[0])[:2]

    left_eye = (
        x + eyes[0][0] + eyes[0][2] // 2,
        y + eyes[0][1] + eyes[0][3] // 2
    )
    right_eye = (
        x + eyes[1][0] + eyes[1][2] // 2,
        y + eyes[1][1] + eyes[1][3] // 2
    )

    return left_eye, right_eye, (x, y, w, h)
