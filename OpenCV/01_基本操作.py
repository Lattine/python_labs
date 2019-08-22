# -*- coding: utf-8 -*-

# @Time    : 2019/8/22
# @Author  : Lattine

# ======================
import cv2

src = cv2.imread("data/dog.png")

# 先定义窗口，后显示图片
cv2.namedWindow("src", cv2.WINDOW_AUTOSIZE)
cv2.imshow("src", src)

cv2.imwrite("data/dog2.png", src)

cv2.waitKey(0)
cv2.destroyAllWindows()
