# -*- coding: utf-8 -*-

# @Time    : 2019/8/14
# @Author  : Lattine

# ======================
import cv2

img = cv2.imread("data/dog.jpg")  # 读入

B, G, R = cv2.split(img)  # 分离
cv2.imshow("Blue", B)
cv2.imshow("Green", G)
cv2.imshow("Red", R)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
print("Stride ", merged.strides)
cv2.imshow("Merged", merged)
cv2.waitKey(0)
