# -*- coding: utf-8 -*-

# @Time    : 2019/8/21
# @Author  : Lattine

# ======================
import cv2

img = cv2.imread("data/house.png")
cv2.namedWindow("house", cv2.WINDOW_AUTOSIZE)
cv2.imshow("house", img)

h, w = img.shape[:2]
print(h, w)

dst1 = cv2.resize(img, (w * 2, h * 2), fx=0.75, fy=0.75, interpolation=cv2.INTER_NEAREST)
cv2.imshow("inter nearest", dst1)

dst2 = cv2.resize(img, (w * 2, h * 2), interpolation=cv2.INTER_LINEAR)
cv2.imshow("inter linear", dst2)

dst3 = cv2.resize(img, (w * 2, h * 2), interpolation=cv2.INTER_CUBIC)
cv2.imshow("inter cubic", dst3)

dst4 = cv2.resize(img, (w * 2, h * 2), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("inter lanczos4", dst4)

cv2.waitKey(0)
cv2.destroyAllWindows()
