import cv2

cap=cv2.VideoCapture(0)
kernel=1

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred=cv2.GaussianBlur(gray,(kernel, kernel),0)

    edges=cv2.Canny(blurred, 50, 150)

    # show kernel size on screen so user knows current blur level
    cv2.putText(edges, f"Blur Kernel: {kernel}x{kernel}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(edges, "Press W for more Blur; Press S for less Blur; Press Esc to Quit", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("Canny Edge Detection", edges)
    cv2.imshow("Original", frame)
    cv2.imshow("Gray", gray)

    key=cv2.waitKey(1)
    if key==27:
        break
    elif key== ord('w'):
        kernel += 2
        print(f"Kernel size increased: {kernel}")
    elif key == ord('s'):
        if kernel>1:
            kernel -= 2
        print(f"Kernel size decreased: {kernel}")

cap.release()
cv2.destroyAllWindows()