# -*- coding: utf-8 -*-

# @Time    : 2019/8/15
# @Author  : Lattine

# ======================
import cv2

img = cv2.imread("data/house.png")  # 读入
cv2.imshow("Origin", img)

# 形态学处理的核心就是定义结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # 定义结构元素

eroded = cv2.erode(img, kernel)  # 腐蚀图像
cv2.imshow("Eroded", img)

dilated = cv2.dilate(img, kernel)  # 膨胀图像
cv2.imshow("Dilated", img)
cv2.waitKey(0)

# 开运算和闭运算就是将腐蚀和膨胀按照一定的次序进行处理。
# 这两者并不是可逆的，即先开后闭并不能得到原先的图像。
# 闭运算用来连接被误分为许多小块的对象，而开运算用于移除由图像噪音形成的斑点。
# 如对一副二值图连续使用闭运算和开运算，将获得图像中的主要对象。
# 如果想消除图像中的噪声（即图像中的“小点”），也可以对图像先用开运算后用闭运算，不过这样也会消除一些破碎的对象。

closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closed", closed)
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opened", opened)

closed_opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)
cv2.imshow("Closed Opened", closed_opened)

opened_closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Opened Closed", opened_closed)
cv2.waitKey(0)

# 检测边缘
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilated = cv2.dilate(img, kernel)
eroded = cv2.erode(img, kernel)
result = cv2.absdiff(dilated, eroded)  # 将两幅图像相减获得边，第一个参数是膨胀后的图像，第二个参数是腐蚀后的图像
retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY)  # 上述结果是灰度图， 将其二值化以便更清楚的观察结果
result = cv2.bitwise_not(result)  # 反色，即对二值化图的每个像素取反
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
