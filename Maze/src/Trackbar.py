'''FINAL ASSIGNMENT CREATIVE TECHNOLOGY 2020 MOD 6 '''
'''German Savchenko s2185091'''
'''AI AND PROGRAMMING'''

import cv2
import numpy as np
n = ""

def nothing(x):
    # any operation
    pass

def init_trackBar(name):
    cv2.namedWindow(name)
    """onChange – Pointer to the function to be called every time the slider changes position. -- NOT REQUIRED, THUS USE nothing"""
    cv2.createTrackbar("L-H", name, 0, 180, nothing)
    cv2.createTrackbar("L-S", name, 66, 255, nothing)
    cv2.createTrackbar("L-V", name, 134, 255,nothing)
    cv2.createTrackbar("U-H", name, 180, 180,nothing)
    cv2.createTrackbar("U-S", name, 255, 255,nothing)
    cv2.createTrackbar("U-V", name, 243, 255,nothing)


def updateTrackbar(name):

    l_h = cv2.getTrackbarPos("L-H", name)
    l_s = cv2.getTrackbarPos("L-S", name)
    l_v = cv2.getTrackbarPos("L-V", name)
    u_h = cv2.getTrackbarPos("U-H", name)
    u_s = cv2.getTrackbarPos("U-S", name)
    u_v = cv2.getTrackbarPos("U-V", name)

    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])

    return lower_red, upper_red

