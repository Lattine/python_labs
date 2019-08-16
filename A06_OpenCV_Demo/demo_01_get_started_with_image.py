# -*- coding: utf-8 -*-

# @Time    : 2019/8/14
# @Author  : Lattine

# ======================
import cv2

# ----------- Read an image
img = cv2.imread("data/dog.png")  # 读入
# cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

# ----------- Display an image
cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # cv2.namedWindow(). By default, the flag is cv2.WINDOW_AUTOSIZE. But if you specify flag to be cv2.WINDOW_NORMAL, you can resize window.
cv2.imshow("image", img)
cv2.waitKey(0)  # cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds.
cv2.destroyAllWindows()  # cv2.destroyAllWindows() simply destroys all the windows we created.

# ----------- Write an image
cv2.imwrite("data/out.png", img)  # First argument is the file name, second argument is the image you want to save.

# ----------- Using Matplotlib
import matplotlib.pyplot as plt

plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.show()
