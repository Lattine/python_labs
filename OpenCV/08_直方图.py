# -*- coding: utf-8 -*-

# @Time    : 2019/8/22
# @Author  : Lattine

# ======================
import cv2
from matplotlib import pyplot as plt

# ------------- 直方图 ------------------
src = cv2.imread("data/table.png")
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([src], [i], None, [256], [0, 256])  # 统计各个颜色通道的直方图
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()

# --------------- 平衡化 -------------------
import numpy as np

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(gray)  # 灰度图平衡化
res1 = np.hstack((gray, equ))
cv2.imshow("res1", res1)

b, g, r = cv2.split(src)
b_equ = cv2.equalizeHist(b)
g_equ = cv2.equalizeHist(g)
r_equ = cv2.equalizeHist(r)
bgr_equ = cv2.merge((b_equ, g_equ, r_equ))
res2 = np.hstack((src, bgr_equ))
cv2.imshow("res2", res2)

# --------------------- CLAHE 自适应均衡化 ---------------------
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
gray2 = clahe.apply(gray)
cv2.imshow("clahe", np.hstack((gray, gray2)))

cv2.waitKey(0)
cv2.destroyAllWindows()
