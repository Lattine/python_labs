# -*- coding: utf-8 -*-

# @Time    : 2019/10/16
# @Author  : Lattine

# ======================


def timer(func):
    """装饰器版本的 计时器"""
    import time

    def wrapper(*args, **kwargs):
        before = time.time()
        res = func(*args, **kwargs)
        after = time.time()
        with open("timer.txt", "a+", encoding="utf-8") as fr:
            print(f"{func.__name__} cost : {after - before}")
            fr.write(f"{func.__name__} cost : {after - before}\n")
        return res

    return wrapper


def time_stamp(t, fmt=r"%Y/%m/%d %H:%M:%S"):
    """将字符串时间，转换为时间数组"""
    import time
    time_struct = time.strptime(t, fmt)
    time_stamp = int(time.mktime(time_struct))
    return time_stamp
