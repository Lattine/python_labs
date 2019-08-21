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


def image_hist(image):
    cv2.imshow("input", image)
    colors = ("blue", "green", "red")
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image],  # 参数必须用方括号
                            [i],  # 参数是用于计算直方图的通道
                            None,  # 参数是Mask，这里没有使用，所以用None
                            [256],  # HistSize表示这个直方图分成多少份（即多少个直方柱）
                            [0., 256.]  # 参数是表示直方图中各个像素的值，[0.0, 256.0]表示直方图能表示像素值从0.0到256的像素
                            )

        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


img = cv2.imread("data/house.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("house", cv2.WINDOW_AUTOSIZE)
cv2.imshow("house", gray)
# custom_hist(gray)
image_hist(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
