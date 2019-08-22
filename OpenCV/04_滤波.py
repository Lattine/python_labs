# -*- coding: utf-8 -*-

# @Time    : 2019/8/22
# @Author  : Lattine

# ======================
import cv2

src = cv2.imread("data/dog.png")
blur = cv2.blur(src, (5, 5))
gaussian = cv2.GaussianBlur(src, (5, 5), 1)
median = cv2.medianBlur(src, 5)
# 9为领域直径，两个75分别是高斯空间核函数标准差，灰度值相似性高斯函数标准差
bilateral = cv2.bilateralFilter(src, 9, 75, 75)

cv2.imshow("origin", src)
cv2.imshow("blur", blur)
cv2.imshow("gaussian", gaussian)
cv2.imshow("median", median)
cv2.imshow("bilateral", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
