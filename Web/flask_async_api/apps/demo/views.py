from concurrent.futures import ThreadPoolExecutor
from . import demo
from app_tasks import tasks

executor = ThreadPoolExecutor()


@demo.route("/")
def index():
    executor.submit(tasks.consumer)  # 调起耗时任务
    return "consumer is ok."
