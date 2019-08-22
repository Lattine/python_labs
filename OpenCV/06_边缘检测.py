# -*- coding: utf-8 -*-

# @Time    : 2019/8/22
# @Author  : Lattine

# ======================
import cv2
import numpy as np

gray = cv2.imread("data/house.png", 0)

# ---------------------- Canny 边缘检测 ---------------------
edges = cv2.Canny(gray, 30, 70)
cv2.imshow("Canny", np.hstack((gray, edges)))

# -------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
