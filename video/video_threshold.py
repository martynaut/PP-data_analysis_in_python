import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('./test_video.mp4')
ret, frame1 = cap.read()

prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[..., 1] = 255
# plt.imshow(hsv)
# plt.show()


while (1):
    ret, frame2 = cap.read()
    if type(frame2) != type(None):
        # frame2[..., 1] = 0 odcięcie pojedynczego koloru
        # frame2[frame2[...,1] < 50 ] = 0 odcięcie poniżej wartości
        # frame2[frame2[...,1] > 250 ] = 0
        frame2[frame2 < 50] = 0
        next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        prvs = next

        # Display the resulting frame
        cv2.imshow('Optical Flow Aura', bgr)
    if cv2.waitKey(2) & 0xFF == ord('q'):  # press q to quit
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
