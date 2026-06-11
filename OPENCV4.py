import cv2
import numpy as np

cap=cv2.VideoCapture(0)

width=int(cap.get(3))
height=int(cap.get(4))

while True:
    ret,frame=cap.read()
    frame = cv2.flip(frame,1)

    half_frame=cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    gray_half=cv2.cvtColor(half_frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original Half", half_frame)
    cv2.imshow("Grayscale Half", gray_half)

    quarter=cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    q_h, q_w=quarter.shape[:2]

    top_left=quarter.copy()
    top_right = cv2.flip(quarter,0)

    hsv=cv2.cvtColor(quarter,cv2.COLOR_BGR2HSV)
    bottom_left=hsv

    pure_red=np.zeros_like(quarter)
    pure_red[:,:,2]=quarter[:,:,2]
    bottom_right=pure_red

    top_row=np.hstack([top_left, top_right])
    bottom_row=np.hstack([bottom_left, bottom_right])
    quad_display=np.vstack([top_row, bottom_row])

    cv2.putText(quad_display, "Original Frame", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    cv2.putText(quad_display, "Flipped Vertically", (q_w + 10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    cv2.putText(quad_display, "HSV Feed", (10, q_h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    cv2.putText(quad_display, "Pure Red Channel", (q_w + 10, q_h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

    cv2.imshow("Quarter View", quad_display)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()