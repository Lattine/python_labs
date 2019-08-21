# -*- coding: utf-8 -*-

# @Time    : 2019/8/21
# @Author  : Lattine

# ======================
import cv2

img1 = cv2.imread("data/dog.png")
img2 = cv2.imread("data/house.png")
img3 = cv2.imread("data/dog.png")
img4 = cv2.imread("data/dog.png")

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.imshow("img4", img4)

hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
hsv3 = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
hsv4 = cv2.cvtColor(img4, cv2.COLOR_BGR2HSV)

hist1 = cv2.calcHist([hsv1], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist2 = cv2.calcHist([hsv2], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist3 = cv2.calcHist([hsv3], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist4 = cv2.calcHist([hsv4], [0, 1], None, [60, 64], [0, 180, 0, 256])

cv2.normalize(hist1, hist1, 0, 1.0, cv2.NORM_MINMAX)
cv2.normalize(hist2, hist2, 0, 1.0, cv2.NORM_MINMAX)
cv2.normalize(hist3, hist3, 0, 1.0, cv2.NORM_MINMAX)
cv2.normalize(hist4, hist4, 0, 1.0, cv2.NORM_MINMAX)

methods = [cv2.HISTCMP_CORREL, cv2.HISTCMP_CHISQR, cv2.HISTCMP_INTERSECT, cv2.HISTCMP_BHATTACHARYYA]
str_method = ""
for method in methods:
    img1_img2 = cv2.compareHist(hist1, hist2, method)
    img3_img4 = cv2.compareHist(hist3, hist4, method)
    if method == cv2.HISTCMP_CORREL:
        str_method = "Correlation"
    if method == cv2.HISTCMP_CHISQR:
        str_method = "Chi-square"
    if method == cv2.HISTCMP_INTERSECT:
        str_method = "Intersection"
    if method == cv2.HISTCMP_BHATTACHARYYA:
        str_method = "Bhattacharyya"

    print("%s src1_src2 = %.2f, src3_src4 = %.2f" % (str_method, img1_img2, img3_img4))

cv2.waitKey(0)
cv2.destroyAllWindows()
