#install libraries
#1. numpy
#2. cvzone
#3. pyserial
#4. mediapipe

import cv2
#import face detection module
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

cam = cv2.VideoCapture(0)                       #0 refers to the camera that must be turned on
detector = FaceDetector(minDetectionCon=0.9)    #0.5 is the standard and varying this will change the
                                                # accuracy of the software
arduino = SerialObject("/dev/cu.usbmodem1431301")


while True:
    success, img = cam.read()
    img, bbox = detector.findFaces(img)

    if bbox:                                      #if face is detected
        arduino.sendData([0, 1, 0])               #send the high signal to the arduino
    else:
        arduino.sendData([1, 0, 0])               #send the low signal if no detection



    cv2.imshow("Image",img)                       #display the face
    cv2.waitKey(1)