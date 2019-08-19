# -*- coding: utf-8 -*-

# @Time    : 2019/8/14
# @Author  : Lattine

# ======================
# -*- coding: utf-8 -*-

# @Time    : 2019/8/14
# @Author  : Lattine

# ======================
import cv2

src = "data/house.png"
img = cv2.imread(src)
cv2.namedWindow("house", cv2.WINDOW_AUTOSIZE)
cv2.imshow("house", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("data/gray.png", gray)
cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
