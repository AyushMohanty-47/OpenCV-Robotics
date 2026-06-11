import cv2
import mediapipe as mp
import numpy as np

cap=cv2.VideoCapture(0)

width=int(cap.get(3))
height=int(cap.get(4))

canvas=np.ones((height, width, 3), dtype=np.uint8)*255

mp_hands=mp.solutions.hands
mp_draw=mp.solutions.drawing_utils
hands=mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)

prev_x,prev_y= 0,0
draw_color=(0,0,255)
brush_size=5

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)

    rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result=hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            x=int(hand_landmarks.landmark[8].x * width)
            y=int(hand_landmarks.landmark[8].y * height)

            if prev_x==0 and prev_y==0:
                prev_x,prev_y=x,y

            cv2.line(canvas, (prev_x, prev_y), (x,y),draw_color, brush_size)
            prev_x,prev_y=x,y

    else:
        prev_x,prev_y= 0,0

    cv2.putText(frame,"Press S to Save; Press C to Clear Press Esc to Quit",(10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255, 255, 255),2)
    troy=(canvas<255)
    frame[troy]=canvas[troy]
    cv2.imshow("Virtual Drawing Board",frame)
    cv2.imshow("Drawing",canvas)

    key=cv2.waitKey(1)
    if key==27:
        break
    elif key==ord('s'):
        cv2.imwrite("paint.png",canvas)
        print("saved as drawing.png")
    elif key==ord('c'):
        canvas=np.zeros((height,width,3), dtype=np.uint8)
        print("screen cleared")

cap.release()
cv2.destroyAllWindows()