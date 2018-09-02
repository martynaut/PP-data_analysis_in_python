import cv2
import matplotlib.pyplot as plt


cap = cv2.VideoCapture('./test_video.mp4')

i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if type(frame) != type(None):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        plt.imshow(image)
        plt.show()
    else:
        cap.release()
    i+=1

cv2.destroyAllWindows()
plt.close('all')