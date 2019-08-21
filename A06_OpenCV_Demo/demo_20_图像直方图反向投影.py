# -*- coding: utf-8 -*-

# @Time    : 2019/8/21
# @Author  : Lattine

# ======================
import cv2
import matplotlib.pyplot as plt


def back_projection_demo():
    sample = cv2.imread("data/house.png")
    target = cv2.imread("data/dog.png")
    roi_hsv = cv2.cvtColor(sample, cv2.COLOR_BGR2HSV)
    target_hsv = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

    cv2.imshow("sample", sample)
    cv2.imshow("target", target)

    roi_hist = cv2.calcHist([roi_hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])
    cv2.normalize(roi_hist, roi_hsv, 0, 255, cv2.NORM_MINMAX)
    dst = cv2.calcBackProject([target_hsv], [0, 1], roi_hist, [0, 180, 0, 256], 1)
    cv2.imshow("back projection demo", dst)


back_projection_demo()

cv2.waitKey(0)
cv2.destroyAllWindows()
