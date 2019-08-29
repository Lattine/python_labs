# -*- coding: utf-8 -*-

# @Time    : 2019/8/28
# @Author  : Lattine

# ======================
import cv2
import numpy as np

src = cv2.imread("data/id.jpg")
mask = cv2.inRange(src, np.array([0, 0, 0]), np.array([193, 193, 193]))
mask_morph = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10)))
contours, hierarchy = cv2.findContours(mask_morph, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    cnt = contours[i]
    rect = cv2.minAreaRect(cnt)
    box = np.int0(cv2.boxPoints(rect))

    height = abs(box[0][1] - box[2][1])
    width = abs(box[0][0] - box[2][0])

    if 1 < width / height < 2:
        print(width / height, width, height)
        print(box[1], box[2], box[0], box[2])
        pts1 = np.float32([box[1], box[2], box[0], box[3]])  # 原图的四个点
        pts2 = np.float32([[0, 0], [450, 0], [0, 300], [450, 300]])  # 输出图像的四个顶点
        M = cv2.getPerspectiveTransform(pts1, pts2)  # 变换
        res = cv2.warpPerspective(src, M, (450, 300))
        cv2.imwrite(f"id_{i}.png", res)
