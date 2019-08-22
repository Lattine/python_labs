# -*- coding: utf-8 -*-

# @Time    : 2019/8/22
# @Author  : Lattine

# ======================
import cv2

src = cv2.imread("data/dog.png")

# ------------- 缩放 --------------
# 指定高度、宽度缩放图片
res1 = cv2.resize(src, (400, 300))
# 指定比例缩放，如x、y放大0.5倍
res2 = cv2.resize(src, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow("res1", res1)
cv2.imshow("res2", res2)
cv2.waitKey(0)

# ------------- 翻转 --------------
res3 = cv2.flip(src, 1)
cv2.imshow("res3", res3)
cv2.waitKey(0)

# ------------- 平移 --------------
import numpy as np

src = cv2.imread("data/house.png")
h, w = src.shape[:2]

# 定义平移矩阵，需要是numpy的float32类型
# x轴平移100，y轴平移50
M = np.float32([[1, 0, 100], [0, 1, 50]])
res4 = cv2.warpAffine(src, M, (h, w))  # 图像、变换矩阵、变换后的大小
cv2.imshow("res4", res4)
cv2.waitKey(0)

# ------------- 平移 --------------
src = cv2.imread("data/house.png")
h, w = src.shape[:2]
M = cv2.getRotationMatrix2D((w / 2, h / 2), 45, 0.5)  # 45°旋转图片并缩小一半
res5 = cv2.warpAffine(src, M, (h, w))
cv2.imshow("res5", res5)
cv2.waitKey(0)

# ------------- 透视变换 --------------
src = cv2.imread("data/house.png")

pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])  # 原图的四个点
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])  # 输出图像的四个顶点

M = cv2.getPerspectiveTransform(pts1, pts2)  # 变换
res6 = cv2.warpPerspective(src, M, (300, 300))
cv2.imshow("res6", res6)
cv2.waitKey(0)

cv2.destroyAllWindows()
