import cv2
from time import sleep

cap = cv2.VideoCapture('./test_video.mp4')
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame', frame)
        sleep(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()