import cv2
import numpy as np

def compute_glasses_position(left_eye, right_eye, face_box, glasses_img):

    fx, fy, fw, fh = face_box
    glasses_width = int(fw * 1.30)

    aspect = glasses_img.shape[0] / glasses_img.shape[1]
    glasses_height = int(glasses_width * aspect)

    eye_center_x = (left_eye[0] + right_eye[0]) // 2
    eye_center_y = (left_eye[1] + right_eye[1]) // 2

    nose_bridge_y = int(eye_center_y + fh * 0.06)

    x = int(eye_center_x - glasses_width / 2)
    y = int(nose_bridge_y - glasses_height * 0.45)

    return x, y, glasses_width, glasses_height


def overlay_glasses(face_img, glasses_img, x, y, gw, gh):
    h, w, _ = face_img.shape

    glasses_resized = cv2.resize(glasses_img, (gw, gh), cv2.INTER_AREA)

    x1 = max(0, x)
    y1 = max(0, y)
    x2 = min(w, x + gw)
    y2 = min(h, y + gh)

    if x1 >= x2 or y1 >= y2:
        return face_img

    overlay = glasses_resized[y1-y:y2-y, x1-x:x2-x]

    if overlay.shape[2] != 4:
        return face_img

    alpha = overlay[:, :, 3] / 255.0
    alpha = alpha[:, :, None]

    face_img[y1:y2, x1:x2] = (alpha * overlay[:, :, :3] + (1 - alpha) * face_img[y1:y2, x1:x2]).astype("uint8")

    return face_img
