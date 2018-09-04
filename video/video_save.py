import cv2

cap = cv2.VideoCapture('./test_video.mp4')

out = cv2.VideoWriter('output2.avi', -1, 10.0, (640,480))

while(cap.isOpened()):
    for i in range(0,8):
        ret, frame = cap.read()
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)
        frame = cv2.resize(frame, (640, 480))
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()