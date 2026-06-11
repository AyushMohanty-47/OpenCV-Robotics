import cv2
import mediapipe as mp
import math

cap=cv2.VideoCapture(0)

mp_hands=mp.solutions.hands
mp_draw=mp.solutions.drawing_utils
hands=mp_hands.Hands(min_detection_confidence=0.7, max_num_hands=2)

led_on=False
PINCH_THRESHOLD=50
past_pinching=False

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)

    height,width=frame.shape[:2]

    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=hands.process(rgb)
    pinching = False

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_x=int(hand_landmarks.landmark[8].x * width)
            index_y=int(hand_landmarks.landmark[8].y * height)

            thumb_x=int(hand_landmarks.landmark[4].x * width)
            thumb_y=int(hand_landmarks.landmark[4].y * height)

            distance = math.sqrt((index_x - thumb_x)**2 + (index_y - thumb_y)**2)

            cv2.line(frame, (thumb_x, thumb_y), (index_x, index_y), (255, 255, 0), 2)
            cv2.putText(frame, f"Dist: {int(distance)}", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

            if distance<PINCH_THRESHOLD:
                pinching=True

    if pinching and not past_pinching:
        led_on=not led_on
        print(f"LED toggled: {'ON' if led_on else 'OFF'}")

    past_pinching = pinching

    led_color=(0,255,0) if led_on else (0,0,255)
    led_label="ON" if led_on else "OFF"

    cv2.circle(frame,(width-60,60),30,led_color,-1)
    cv2.putText(frame,led_label,(width-75,65),
                cv2.FONT_HERSHEY_SIMPLEX,0.7, (0,0,0),2)

    cv2.putText(frame,"If Pinch<30, toggle LED; Press Esc to quit",(10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("LED Indicator",frame)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()