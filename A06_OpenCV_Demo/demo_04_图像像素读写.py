# -*- coding: utf-8 -*-

# @Time    : 2019/8/15
# @Author  : Lattine

# ======================
import cv2

img = cv2.imread("data/house.png")  # 读入
cv2.namedWindow("house", cv2.WINDOW_AUTOSIZE)
cv2.imshow("house", img)

h, w, ch = img.shape
print(f"height: {h}, width: {w}, channel: {ch}")
for raw in range(h):
    for col in range(w):
        b, g, r = img[raw, col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        img[raw, col] = (b, g, r)

cv2.imshow("output", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
