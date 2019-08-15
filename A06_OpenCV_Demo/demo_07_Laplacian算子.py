# -*- coding: utf-8 -*-

# @Time    : 2019/8/15
# @Author  : Lattine

# ======================
# 图像中的边缘区域，像素值会发生“跳跃”，对这些像素求导，在其一阶导数在边缘位置为极值，这就是Sobel算子使用的原理——极值处就是边缘。
# 如果对像素值求二阶导数，会发现边缘处的导数值为0。Laplace函数实现的方法是先用Sobel 算子计算二阶x和y导数，再求和。
import cv2

img = cv2.imread("data/house.png", 0)  # 读入
cv2.imshow("Origin", img)

dst = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
dst = cv2.convertScaleAbs(dst)
cv2.imshow("DST", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
