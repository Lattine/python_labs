# -*- coding: utf-8 -*-

# @Time    : 2019/8/21
# @Author  : Lattine

# ======================
import cv2
import numpy as np
import matplotlib.pyplot as plt


def custom_hist(gray):
    h, w = gray.shape
    hist = np.zeros([256], dtype=np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1

    y_pos = np.arange(0, 256, 1, dtype=np.int32)
    plt.bar(y_pos, hist, align="center", color="r", alpha=0.5)
    plt.xticks(y_pos, y_pos)
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()


img = cv2.imread("data/house.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("house", cv2.WINDOW_AUTOSIZE)
cv2.imshow("house", gray)
dst = cv2.equalizeHist(gray)
cv2.imshow("dst", dst)

custom_hist(gray)
custom_hist(dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
