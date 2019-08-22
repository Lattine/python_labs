# -*- coding: utf-8 -*-

# @Time    : 2019/8/22
# @Author  : Lattine

# ======================
import cv2
import numpy as np

src = cv2.imread("data/table.png")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
gray = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("gray", gray)
# --------------------------- 霍夫直线检测 -----------------------
edges = cv2.Canny(gray, 50, 150)
lines = cv2.HoughLines(edges, 0.8, np.pi / 180, 90)
res1 = src.copy()
if lines is None: lines = []
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(res1, (x1, y1), (x2, y2), (0, 0, 255))

cv2.imshow("res1", res1)

# --------------------------- 霍夫直线概率检测 -----------------------
lines = cv2.HoughLinesP(edges, 0.8, np.pi / 180, 90, minLineLength=50, maxLineGap=10)
res2 = src.copy()
if lines is None: lines = []
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(res2, (x1, y1), (x2, y2), (0, 0, 255), 1, lineType=cv2.LINE_AA)

cv2.imshow("res2", res2)

# --------------------------- 霍夫圆概率检测 -----------------------
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param2=20)
circles = np.int0(np.round(circles))
res3 = src.copy()
for i in circles[0, :]:
    cv2.circle(res3, (i[0], i[1]), i[2], (0, 255, 0), 2)  # 画出外圆
    cv2.circle(res3, (i[0], i[1]), 2, (0, 0, 255), 3)
cv2.imshow("res3", res3)
cv2.waitKey(0)

cv2.destroyAllWindows()
