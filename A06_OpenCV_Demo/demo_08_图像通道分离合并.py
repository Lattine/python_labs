# -*- coding: utf-8 -*-

# @Time    : 2019/8/15
# @Author  : Lattine

# ======================
import cv2

img = cv2.imread("data/house.png")
cv2.namedWindow("house", cv2.WINDOW_AUTOSIZE)
cv2.imshow("house", img)

# Blue is 0
mv = cv2.split(img)
mv[0][:, :] = 0
dst1 = cv2.merge(mv)
cv2.imshow("Blue", dst1)

# Green is 0
mv = cv2.split(img)
mv[1][:, :] = 0
dst2 = cv2.merge(mv)
cv2.imshow("Green", dst2)

# Red is 0
mv = cv2.split(img)
mv[2][:, :] = 0
dst3 = cv2.merge(mv)
cv2.imshow("Red", dst3)

# 混合通道（没效果？)
cv2.mixChannels(img, dst3, [0, 1])
cv2.imshow("Mix", dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()
