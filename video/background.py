import cv2
from time import sleep

alpha = 0.999
isFirstTime = True
cap = cv2.VideoCapture('./test_video.mp4')
i = 0
while (True):
    i += 1
    ret, frame = cap.read()
    if i < 8:
        continue
    else:
        if type(frame) != type(None):
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            if isFirstTime==True:
               bg_img=frame
               isFirstTime=False
            else:
               bg_img = cv2.addWeighted(frame,(1-alpha),bg_img,alpha,0)

            fg_img = cv2.absdiff(frame, bg_img)

            cv2.imshow('Video Capture', frame)
            cv2.imshow('Background', bg_img)
            cv2.imshow('Foreground', fg_img)
            sleep(0.5)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()