import cv2


cap = cv2.VideoCapture('./test_video.mp4')
while (cap.isOpened()):
    ret, frame = cap.read()
    print(ret, frame)
    if ret == True:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # small = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        small = cv2.resize(img, (1000, 500))
        cv2.imshow('Grey', small)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()