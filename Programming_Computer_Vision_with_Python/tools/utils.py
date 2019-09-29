# -*- coding: utf-8 -*-

# @Time    : 2019/9/23
# @Author  : Lattine

# ======================
import os
import numpy as np


def get_imlist(path, end="jpg"):
    """获取文件夹下所有特定格式的图片"""
    end = "." + end
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(end)]


def hist_equation(im, nbr_bins=256):
    """对一幅灰度图像进行直方图均衡化"""
    # 计算图像的直方图
    imhist, bins = np.histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()  # 累积分布函数 cumulative distribution function
    cdf = 255 * cdf / cdf[-1]  # 归一化
    # 使用累积分布函数的线性插值，计算新的像素值
    im2 = np.interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf
