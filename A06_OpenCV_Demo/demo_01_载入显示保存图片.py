# -*- coding: utf-8 -*-

# @Time    : 2019/8/14
# @Author  : Lattine

# ======================
import cv2

img = cv2.imread("data/dog.jpg")  # 读入
cv2.imshow("Dog", img)  # 显示
cv2.waitKey(0)  # 暂停

# 复制
img2 = img.copy()
cv2.imshow("Dog2", img2)
cv2.waitKey(0)

# 保存图像
cv2.imwrite("data/og-copy.jpg", img2)
