import numpy as np
import cv2
import os

cam=cv2.VideoCapture(0)

c=0

while(True):
    ret,frame=cam.read()

    if c==150:
        name="frame"+str(c)+".jpg"
        print("Creating..."+name)

        cv2.imwrite(name, frame)
        break

    c+=1
cam.release()
cv2.destroyAllWindows