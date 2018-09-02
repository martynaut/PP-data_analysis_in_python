import cv2


kernelSize=21   # Kernel Bluring size

# Edge Detection Parameter
parameter1=20
parameter2=20
intApertureSize=10

cap = cv2.VideoCapture('./test_video.mp4')
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.GaussianBlur(frame, (kernelSize, kernelSize), 0, 0)
        frame = cv2.Canny(frame, parameter1, parameter2, intApertureSize)
        cv2.imshow('Grey', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()