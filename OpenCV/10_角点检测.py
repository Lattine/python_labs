# -*- coding: utf-8 -*-

# @Time    : 2019/8/23
# @Author  : Lattine

# ======================
import cv2
import numpy as np


def harris(image, opt=1):
    block_size = 2
    aperture_size = 3
    k = 0.04
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # ------------ Harris角点检测
    dst = cv2.cornerHarris(gray, block_size, aperture_size, k)
    dst_norm = np.empty(dst.shape, dtype=np.float32)
    cv2.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    print(len(dst))

    # ------------ Shi-Tomas角点检测
    corners = cv2.goodFeaturesToTrack(gray, 35, 0.05, 10)
    print(len(corners))

    # ------------ 亚像素级的角点检测
    # detect sub-pixel
    winSize = (3, 3)
    zeroZone = (-1, -1)
    # Stop condition
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_COUNT, 40, 0.001)
    # Calculate the refined corner locations
    corners = cv2.cornerSubPix(gray, corners, winSize, zeroZone, criteria)
    print(len(corners))

    for pt in corners:
        print(pt)
        b = np.random.random_integers(0, 256)
        g = np.random.random_integers(0, 256)
        r = np.random.random_integers(0, 256)
        x = np.int32(pt[0][0])
        y = np.int32(pt[0][1])
        cv2.circle(image, (x, y), 5, (int(b), int(g), int(r)), 2)

    for i in range(dst_norm.shape[0]):
        for j in range(dst_norm.shape[1]):
            if int(dst_norm[i, j]) > 120:
                cv2.circle(image, (j, i), 2, (0, 255, 0), 2)

    return image


src = cv2.imread("data/table.png")
cv2.imshow("src", src)
result = harris(src)
cv2.imshow("result", result)
cv2.imwrite("result.png", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
