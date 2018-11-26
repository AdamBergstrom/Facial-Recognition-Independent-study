import cv2
import numpy as np
import os

FPS = 30
# Playing video from file:
cap = cv2.VideoCapture('/Users/adambergstrom/Desktop/499-rekognition/venv/01-01-01-01-01-01-01.mp4')
cap.set(cv2.CAP_PROP_FPS, FPS)

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret: break
    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()