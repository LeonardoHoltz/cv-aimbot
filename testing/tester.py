from turtle import screensize
import cv2 as cv
import time
import sys
from vision import Vision

sys.path.append('..')

from common.window_capture import WindowCapture

wcap = WindowCapture('Counter-Strike: Global Offensive - Direct3D 9')

model = cv.CascadeClassifier('../cascade_classifier/training/cascade.xml')

vision = Vision(None)

while(True):

    screenshot = wcap.get_screenshot()

    rectangles = model.detectMultiScale(screenshot)
    
    detection_image = vision.draw_rectangles(screenshot, rectangles)

    # display the images
    cv.imshow('Matches', detection_image)

    key = cv.waitKey(1)
    if key == ord('q'):
        # End
        cv.destroyAllWindows()
        break


