#install libraries
#1. numpy
#2. cvzone
#3. pyserial
#4. mediapipe

import cv2
#import face detection module
from cvzone.FaceDetectionModule import FaceDetector

cam = cv2.VideoCapture(0)                       #0 refers to the camera that must be turned on
detector = FaceDetector(minDetectionCon=0.5)    #0.5 is the standard and varying this will change the
                                                # accuracy of the software

while True:
    success, img = cam.read()
    img, bbox = detector.findFaces(img)

    cv2.imshow("Image",img)                     #display the face
    cv2.waitKey(1)