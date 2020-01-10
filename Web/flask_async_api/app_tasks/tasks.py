import time


def consumer():
    """模拟耗时消费任务"""
    time.sleep(1)
    print(f"task is cost time ...")
    time.sleep(10)
    print(f"task is done.")