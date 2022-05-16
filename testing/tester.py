from ctypes import WinDLL
from turtle import screensize
import cv2 as cv
import time
import sys
from vision import Vision
import win32api
import math
import pyautogui
import win32api, win32con
import keyboard

sys.path.append('..')

from common.window_capture import WindowCapture

def GetSmallestRectangle(rectangles):
    smallest_area = math.inf
    smallest_rect = []
    for rect in rectangles:
        area = rect[2] * rect[3]
        if area < smallest_area:
            smallest_area = area
            smallest_rect = rect
    return smallest_rect

wcap = WindowCapture('Counter-Strike: Global Offensive - Direct3D 9')

model = cv.CascadeClassifier('../cascade_classifier/training_results/training4/cascade.xml')
#model = cv.CascadeClassifier('../cascade_classifier/training_results/pedestrian_detection/haarcascade_fullbody.xml')

vision = Vision(None)

middle_window_w = math.floor(852 / 4)
middle_window_h = math.floor(480 / 4)

aimbotOn = False

while(True):

    screenshot = wcap.get_screenshot()

    rectangles = model.detectMultiScale(screenshot)

    #print(rectangles)

    if len(rectangles) > 0 and aimbotOn:
        rectangle = GetSmallestRectangle(rectangles)
        x = rectangle[0]
        y = rectangle[1]
        w = rectangle[2]
        h = rectangle[3]
        rect_mid_x = math.floor((x + (w/2)) / 2)
        rect_mid_y = math.floor((y + (h/2)) / 2)

        x_offset = rect_mid_x - middle_window_w
        y_offset = rect_mid_y - middle_window_h
        
        # Move by offset
        #win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(x_offset/win32api.GetSystemMetrics(0)*65535), int(y_offset/win32api.GetSystemMetrics(1)*65535) ,0 ,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, x_offset * 4, y_offset * 4, 0, 0)

    detection_image = vision.draw_rectangles(screenshot, rectangles)

    # display the images
    cv.imshow('Matches', detection_image)

    key = cv.waitKey(1)
    if key == ord('q'):
        # End
        cv.destroyAllWindows()
        break

    elif key == ord('c'):
        aimbotOn = not aimbotOn
        print("aaa")


