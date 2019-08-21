# -*- coding: utf-8 -*-

# @Time    : 2019/8/21
# @Author  : Lattine

# ======================
import cv2
import numpy as np

img = np.zeros((512, 512, 3), dtype=np.uint8)

cv2.rectangle(img, (100, 100), (300, 300), (255, 0, 0), 2, cv2.LINE_8, 0)
cv2.circle(img, (256, 256), 50, (0, 0, 255), 2, cv2.LINE_8, 0)
cv2.ellipse(img, (256, 256), (150, 50), 360, 0, 360, (0, 255, 0), 2, cv2.LINE_8, 0)

cv2.imshow("img", img)
cv2.waitKey(0)
