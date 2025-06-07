import cv2 
import numpy as np

camset = "udpsrc port=5000 ! application/x-rtp, encoding-name=H264 ! rtph264depay ! avdec_h264 ! videoconvert ! appsink"


cam = cv2.VideoCapture(camset)

while True:

    _, frame = cam.read()

    frame = cv2.flip(frame, -1)
    cv2.imshow("VidStream", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()