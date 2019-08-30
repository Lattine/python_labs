# -*- coding: utf-8 -*-

# @Time    : 2019/8/29
# @Author  : Lattine

# ======================
import cv2
import numpy as np


# 仿射提取表格
def affine_correction(src):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if not contours: return src
    max_area = -1
    max_idx = -1
    for i, c in enumerate(contours):
        area = cv2.contourArea(c)
        if max_area < area:
            max_area = area
            max_idx = i
    approx = cv2.approxPolyDP(contours[max_idx], 10, True)  # 逼近区域成为一个形状
    # mg_cont = cv2.drawContours(src, [approx], -1, (0, 0, 255), 2)  # 画出轮廓
    pts1 = np.float32([approx[0][0], approx[1][0], approx[2][0], approx[3][0]])  # 原图的四个点
    (h, w) = (approx[1][0][1] - approx[0][0][1], approx[2][0][0] - approx[1][0][0])
    pts2 = np.float32([[0, 0], [0, h], [w, h], [w, 0]])  # 输出图像的四个顶点
    M = cv2.getPerspectiveTransform(pts1, pts2)  # 变换
    binary = cv2.warpPerspective(src, M, (w, h))

    return cv2.merge((binary, binary, binary))


# 旋转纠正歪斜页面
def rotation_correct(src):
    # 度数转换
    def degree_trans(theta):
        res = theta / np.pi * 180
        return res

    # 通过霍夫变换计算角度
    def calc_degree(src):
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 1))
        mid = cv2.erode(thresh, kernel, iterations=5)

        dst_image = cv2.Canny(mid, 50, 200, 3)

        # 通过霍夫变换检测直线
        # 第4个参数就是阈值，阈值越大，检测精度越高
        lines = cv2.HoughLines(dst_image, 1, np.pi / 180, 200)

        sum = 0
        for i in range(len(lines)):
            for rho, theta in lines[i]:
                sum += theta

        # 对所有角度求平均，这样做旋转效果会更好
        average = sum / len(lines)
        angle = degree_trans(average) - 90
        return angle

    # 旋转变换
    def rotate_image(src, degree):
        h, w = src.shape[:2]
        M = cv2.getRotationMatrix2D((w / 2.0, h / 2.0), degree, 1)
        rotate = cv2.warpAffine(src, M, (w, h), borderValue=(255, 255, 255))
        return rotate

    degree = calc_degree(src)
    print("调整角度：", degree)
    rotation = rotate_image(src, degree)
    return rotation
