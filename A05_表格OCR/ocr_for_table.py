# -*- coding: utf-8 -*-

# @Time    : 2019/8/15
# @Author  : Lattine

# ======================
import cv2
import numpy as np


class ImageTableOCR:
    def __init__(self, path):
        self.image = cv2.imread(path)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.scale = 5
        self.threshold = 5

    def cross_point(self):
        blurred = cv2.GaussianBlur(self.gray, (5, 5), 0)
        thresholded = cv2.adaptiveThreshold(~blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)
        raw_img = thresholded.copy()
        raw_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (raw_img.shape[1] // self.scale, 1))
        raw_eroded = cv2.erode(raw_img, raw_kernel, 1)
        raw_dilated = cv2.dilate(raw_eroded, raw_kernel, 1)

        col_img = thresholded.copy()
        col_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, col_img.shape[0] // self.scale))
        col_eroded = cv2.erode(col_img, col_kernel, 1)
        col_dilated = cv2.dilate(col_eroded, col_kernel, 1)

        # mask_img = raw_dilated + col_dilated
        cross_img = cv2.bitwise_and(raw_dilated, col_dilated)
        return cross_img

    def detect_cell(self):
        cross_img = self.cross_point()
        # 切出Cell
        xs, ys = np.where(cross_img > 0)
        x_list = []
        sxs = np.sort(xs)
        for i in range(len(sxs) - 1):
            if sxs[i + 1] - sxs[i] > self.threshold:
                x_list.append(sxs[i])
        x_list.append(sxs[len(sxs) - 1])

        y_list = []
        sys = np.sort(ys)
        for i in range(len(sys) - 1):
            if sys[i + 1] - sys[i] > self.threshold:
                y_list.append(sys[i])
        y_list.append(sys[len(sys) - 1])

        print("x", x_list)
        print("y", y_list)
        for i in range(len(y_list) - 1):
            for j in range(len(x_list) - 1):
                print(self.image.shape, y_list[i], y_list[i + 1], x_list[j], x_list[j + 1])
                roi = self.image[x_list[j]:x_list[j + 1], y_list[i]:y_list[i + 1]]
                cv2.imshow("img", roi)
                cv2.waitKey(0)


if __name__ == '__main__':
    tb = ImageTableOCR("data/demo.png")
    tb.detect_cell()
