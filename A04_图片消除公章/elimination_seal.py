# -*- coding: utf-8 -*-

# @Time    : 2019/8/14
# @Author  : Lattine

# ======================
import os
import argparse
import numpy as np
import cv2


class Image:
    def __init__(self, filename):
        self.filename = filename

    def eliminate_red(self):
        img = cv2.imread(self.filename)
        B, G, R = cv2.split(img)
        R[R[:, :] > 200] = 255
        cv2.imwrite(self.filename + ".em.png", R)


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
