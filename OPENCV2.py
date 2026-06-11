import cv2

cap=cv2.VideoCapture(0)
img_count=0

while True:
    timer=cv2.getTickCount()
    ret,frame=cap.read()

    FPS=cv2.getTickFrequency()/(cv2.getTickCount()-timer+1)

    cv2.putText(frame,f"FPS: {int(FPS)}",(10,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(200,0,200),2)

    cv2.putText(frame,"Press S to save the image feed and Esc to quit",(10, 80),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(255, 255, 255),2)

    cv2.imshow("Live Webcam",frame)

    key=cv2.waitKey(1)
    if key==27:
        break
    elif key==ord('s'):
        filename=f"saved{img_count +1}.png"
        cv2.imwrite(filename,frame)
        print(f"Image saved as {filename}")
        img_count += 1

cap.release()
cv2.destroyAllWindows()