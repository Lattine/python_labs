# -*- coding: utf-8 -*-

# @Time    : 2019/9/27
# @Author  : Lattine

# ======================


def get_box_coord(x, y, w, h, angle):
    """根据左上角坐标和旋转角度，计算旋转后矩形的4个坐标"""
    import math

    # 矩形框中点(x0,y0)
    x0 = x + w / 2
    y0 = y + h / 2
    line = math.sqrt(pow(w / 2, 2) + pow(h / 2, 2))  # 即对角线的一半
    if angle < 0:  # angle小于0，逆时针转
        angle_bg = -angle + math.atan(h / float(w))  # 旋转角度 - 对角线与底线所成的角度
        angle_sm = -angle - math.atan(h / float(w))  # 旋转角度 + 对角线与底线所成的角度
        pt1 = (x0 - line * math.cos(angle_sm), y0 + line * math.sin(angle_sm))  # 左上角
        pt2 = (x0 + line * math.cos(angle_bg), y0 - line * math.sin(angle_bg))  # 右上角
        pt3 = (x0 + line * math.cos(angle_sm), y0 - line * math.sin(angle_sm))  # 右下角
        pt4 = (x0 - line * math.cos(angle_bg), y0 + line * math.sin(angle_bg))  # 左下角
    else:  # angle大于0，顺时针
        angle_bg = angle + math.atan(h / float(w))
        angle_sm = angle - math.atan(h / float(w))
        pt1 = (x0 - line * math.cos(angle_bg), y0 + line * math.sin(angle_bg))  # 左上角
        pt2 = (x0 + line * math.cos(angle_sm), y0 - line * math.sin(angle_sm))  # 右上角
        pt3 = (x0 + line * math.cos(angle_bg), y0 - line * math.sin(angle_bg))  # 右下角
        pt4 = (x0 - line * math.cos(angle_sm), y0 + line * math.sin(angle_sm))  # 左下角
    return pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1], pt4[0], pt4[1]


def get_ordered_point(a, b, c, d):
    """依据四个无序的坐标点， 返回左上，右上，左下，右下顺序的坐标"""
    arr = [a, b, c, d]
    arr.sort(key=lambda x: x[0])
    if arr[0][1] < arr[1][1]:
        left_up = arr[0]
    else:
        left_up = arr[1]
    if arr[3][1] > arr[2][1]:
        right_down = arr[3]
    else:
        right_down = arr[2]
    arr.sort(key=lambda x: x[1])
    if arr[0][0] > arr[1][0]:
        right_up = arr[0]
    else:
        right_up = arr[1]
    if arr[2][0] < arr[3][0]:
        left_down = arr[2]
    else:
        left_down = arr[3]
    return left_up, right_up, left_down, right_down


def pdf2img(path):
    """ PDF扫描件转图片， 基于PyMuPDF插件 """
    import cv2
    import fitz
    import numpy as np

    doc = fitz.open(path)  # 打开PDF文件，doc为Document类型，包含文件所有页的列表

    zoom_x, zoom_y = 4.0, 4.0  # 缩放比例
    rotate = 0
    trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)

    imgs = []
    for pg in range(doc.pageCount):
        page = doc[pg]
        pm = page.getPixmap(matrix=trans, alpha=False)
        png_data = pm.getPNGdata()
        img_array = np.frombuffer(png_data, dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_ANYCOLOR)
        imgs.append(img)
    return imgs
