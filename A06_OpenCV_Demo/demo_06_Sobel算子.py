# -*- coding: utf-8 -*-

# @Time    : 2019/8/15
# @Author  : Lattine

# ======================
# Sobel算子依然是一种过滤器，只是其是带有方向的。
# 在Sobel函数的第二个参数这里使用了cv2.CV_16S。因为OpenCV文档中对Sobel算子的介绍中有这么一句：“in the case of 8-bit input images it will result in truncated derivatives”。
# 即Sobel函数求完导数后会有负值，还有会大于255的值。而原图像是uint8，即8位无符号数，所以Sobel建立的图像位数不够，会有截断。
# 因此要使用16位有符号的数据类型，即cv2.CV_16S。
# 在经过处理后，别忘了用convertScaleAbs()函数将其转回原来的uint8形式。否则将无法显示图像，而只是一副灰色的窗口。
# 由于Sobel算子是在两个方向计算的，最后还需要用cv2.addWeighted(...)函数将其组合起来。
import cv2

img = cv2.imread("data/house.png", 0)  # 读入
cv2.imshow("Origin", img)

x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
abs_x = cv2.convertScaleAbs(x)
abs_y = cv2.convertScaleAbs(y)
dst = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
cv2.imshow("ABS X", abs_x)
cv2.imshow("ABS Y", abs_y)
cv2.imshow("DST", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
