# -*- coding: utf-8 -*-

# @Time    : 2019/8/15
# @Author  : Lattine

# ======================
import cv2
import numpy as np

img = cv2.imread("data/test.png")  # 读入
img = cv2.GaussianBlur(img, (3, 3), 0)
edges = cv2.Canny(img, 100, 300, apertureSize=3)
result = img.copy()

# 经验参数
min_line_length = 200
max_line_Gap = 15
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 80, min_line_length, max_line_Gap)

for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(result, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
