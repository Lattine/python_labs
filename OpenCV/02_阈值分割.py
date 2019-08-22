# -*- coding: utf-8 -*-

# @Time    : 2019/8/22
# @Author  : Lattine

# ======================
import cv2

import matplotlib.pyplot as plt

# ------------------------- 固定阈值分割 ---------------------------
src = cv2.imread("data/table.png")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

ret, th1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [gray, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i], fontsize=8)
    plt.xticks([])
    plt.yticks([])
plt.show()

# ------------------------- 自适应阈值分割 ---------------------------
src = cv2.imread("data/dog.png")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
auto_th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
plt.imshow(auto_th, cmap="gray")
plt.show()

# ------------------------- QTSU 阈值分割 ---------------------------

src = cv2.imread("data/dog.png")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 固定阈值
ret1, th1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# QTSU
ret2, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 先高斯滤波，再用QTSU分割
blur = cv2.GaussianBlur(gray, (5, 5), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

images = [gray, 0, th1, gray, 0, th2, blur, 0, th3]
titles = ['Original', 'Histogram', 'Global(v=100)',
          'Original', 'Histogram', "Otsu's",
          'Gaussian filtered Image', 'Histogram', "Otsu's"]

for i in range(3):
    # 绘制原图
    plt.subplot(3, 3, i * 3 + 1)
    plt.imshow(images[i * 3], 'gray')
    plt.title(titles[i * 3], fontsize=8)
    plt.xticks([]), plt.yticks([])
    # 绘制直方图plt.hist，ravel函数将数组降成一维
    plt.subplot(3, 3, i * 3 + 2)
    plt.hist(images[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1], fontsize=8)
    plt.xticks([]), plt.yticks([])
    # 绘制阈值图
    plt.subplot(3, 3, i * 3 + 3)
    plt.imshow(images[i * 3 + 2], 'gray')
    plt.title(titles[i * 3 + 2], fontsize=8)
    plt.xticks([]), plt.yticks([])
plt.show()
