import cv2
import mediapipe as mp
import numpy as np


def create_face_mask(img_shape, boxes, expand_k=0.35):
    h, w = img_shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)

    for (x1, y1, x2, y2) in boxes:
        bw = x2 - x1
        bh = y2 - y1

        # šiek tiek padidinam dėžutę aplink veidą
        ex1 = max(0, int(x1 - bw * expand_k))
        ey1 = max(0, int(y1 - bh * expand_k))
        ex2 = min(w, int(x2 + bw * expand_k))
        ey2 = min(h, int(y2 + bh * expand_k))

        cx = (ex1 + ex2) // 2
        cy = (ey1 + ey2) // 2

        axis_x = (ex2 - ex1) // 2
        axis_y = int((ey2 - ey1) * 0.6)

        cv2.ellipse(
            mask,
            (cx, cy),
            (axis_x, axis_y),
            0,
            0, 360,
            255,
            -1
        )

    mask = cv2.GaussianBlur(mask, (51, 51), 0)
    return mask


def main():
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(
        static_image_mode=False,
        max_num_faces=5,
        refine_landmarks=False,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Nepavyko atidaryti kameros.")
        return

    print("Spausk 'c' – išsaugoti nuotrauką, 'q' – išeiti.")
    photo_counter = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w, _ = frame.shape

        # BGR -> RGB mediapipe'ui
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        boxes = []

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                xs = [lm.x * w for lm in face_landmarks.landmark]
                ys = [lm.y * h for lm in face_landmarks.landmark]

                min_x = int(max(min(xs), 0))
                max_x = int(min(max(xs), w))
                min_y = int(max(min(ys), 0))
                max_y = int(min(max(ys), h))

                boxes.append((min_x, min_y, max_x, max_y))

        # stiprus blur visam kadrui
        blurred_full = cv2.GaussianBlur(frame, (101, 101), 0)

        if boxes:
            mask_gray = create_face_mask(frame.shape, boxes, expand_k=0.35)
            mask = cv2.merge([mask_gray, mask_gray, mask_gray])
            mask_inv = cv2.bitwise_not(mask)

            face_blurred = cv2.bitwise_and(blurred_full, mask)
            background = cv2.bitwise_and(frame, mask_inv)
            result = cv2.add(face_blurred, background)
        else:
            result = frame

        cv2.imshow("Blur Face (FaceMesh, strong blur)", result)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            filename = f"blurred_facemesh_{photo_counter}.jpg"
            cv2.imwrite(filename, result)
            print("Išsaugota:", filename)
            photo_counter += 1

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
