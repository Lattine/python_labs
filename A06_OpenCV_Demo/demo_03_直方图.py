# -*- coding: utf-8 -*-

# @Time    : 2019/8/14
# @Author  : Lattine

# ======================
import cv2
import numpy as np


# hist = cv2.calcHist([img],
#                     [0],  # 用于计算直方图的通道
#                     None,  # Mask,
#                     [256],  # histSize，表示这个直方图分成多少份（即多少个直方柱）
#                     [0.0, 255.0]  # 表示直方图中各个像素的值，[0.0, 255.0]表示直方图能表示像素值从0.0到255的像素。
#                     )
def calc_and_draw_hist(img, color):
    hist = cv2.calcHist([img], [0], None, [256], [0.0, 255.0])
    minval, maxval, minloc, maxloc = cv2.minMaxLoc(hist)
    hist_img = np.zeros([256, 256, 3], np.uint8)
    hpt = int(0.9 * 256)
    for h in range(256):
        intensity = int(hist[h] * hpt / maxval)
        cv2.line(hist_img, (h, 256), (h, 256 - intensity), color)
    return hist_img


if __name__ == '__main__':
    img = cv2.imread("data/dog.jpg")  # 读入

    B, G, R = cv2.split(img)  # 分离
    hist_img_B = calc_and_draw_hist(B, [255, 0, 0])
    hist_img_G = calc_and_draw_hist(G, [0, 255, 0])
    hist_img_R = calc_and_draw_hist(R, [0, 0, 255])
    cv2.imshow("B", hist_img_B)
    cv2.imshow("G", hist_img_G)
    cv2.imshow("R", hist_img_R)
    cv2.waitKey(0)
