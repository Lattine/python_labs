# -*- coding: utf-8 -*-

# @Time    : 2019/8/14
# @Author  : Lattine

# ======================
import os
import argparse

import cv2 as cv


class Image:
    def __init__(self, filename):
        self.filename = filename

    def eliminate_red(self):
        img = cv.imread(self.filename)
        # Python是GBR的顺序
        # G = img[:, :, 0]
        # B = img[:, :, 1]
        R = img[:, :, 2]
        row, col = R.shape
        for i in range(row):
            for j in range(col):
                if R[i, j] > 220:
                    R[i, j] = 255
                else:
                    continue

        cv.imwrite(self.filename + ".em.png", R)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, default="data", help="PDF path.")

    args = parser.parse_args()
    base_dir = args.path
    for root, dirs, files in os.walk(base_dir):
        for fn in files:
            if ".em." not in fn:
                em = Image(os.path.join(base_dir, fn))
                em.eliminate_red()
