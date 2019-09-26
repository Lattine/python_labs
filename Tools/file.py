# -*- coding: utf-8 -*-

# @Time    : 2019/9/26
# @Author  : Lattine

# ======================
import os


def remove_files(path):
    """删除目录下所有文件，包含子目录"""
    for fn in os.listdir(path):
        fpath = os.path.join(path, fn)  # 构造文件路径
        if os.path.isfile(fpath):  # 文件
            os.remove(fpath)
        else:  # 文件夹
            remove_files(fpath)  # 递归的删除子文件夹
