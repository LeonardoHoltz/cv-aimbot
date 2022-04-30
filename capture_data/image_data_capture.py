from turtle import screensize
import cv2 as cv
import time
from common.window_capture import WindowCapture

wcap = WindowCapture('Counter Strike: Global Offensive - Direct3D 9')
loop_time = time.time()

while(True):

    screenshot = wcap.get_screenshot()

    cv.imshow("screenshot", screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time.time() - loop_time)))
    loop_time = time.time()

    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('u'):
        # Set negative image data
        cv.imwrite('../dataset/negative/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('j'):
        # Set positive image data
        cv.imwrite('../dataset/positive{}.jpg'.format(loop_time), screenshot)

