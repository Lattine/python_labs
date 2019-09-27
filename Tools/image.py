# -*- coding: utf-8 -*-

# @Time    : 2019/9/27
# @Author  : Lattine

# ======================
import math


def get_box_coord(x, y, w, h, angle):
    """根据左上角坐标和旋转角度，计算旋转后矩形的4个坐标"""

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
