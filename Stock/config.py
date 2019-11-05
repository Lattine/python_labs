# -*- coding: utf-8 -*-

# @Time    : 2019/11/4
# @Author  : Lattine

# ======================
import os


class Config:
    BASE_URL = os.path.abspath(os.getcwd())
    codes_hub = "https://xueqiu.com/service/v5/stock/screener/quote/list"
    news_hub = "https://xueqiu.com/statuses/stock_timeline.json"
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'aliyungf_tc=AQAAAOtGklSxGQwAUhVFeTaV3wKjdope; xq_a_token=584d0cf8d5a5a9809761f2244d8d272bac729ed4; xq_a_token.sig=x0gT9jm6qnwd-ddLu66T3A8KiVA; xq_r_token=98f278457fc4e1e5eb0846e36a7296e642b8138a; xq_r_token.sig=2Uxv_DgYTcCjz7qx4j570JpNHIs; _ga=GA1.2.557243314.1534335292; _gid=GA1.2.1222731268.1534335292; _gat_gtag_UA_16079156_4=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1534335293; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1534335293; u=121534335293404; device_id=4633cb10d0c99f1a3733f5feb4427c50',
        'Host': 'xueqiu.com',
        'Referer': 'https://xueqiu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data_path = os.path.join(BASE_URL, "data")


config = Config()
if not os.path.exists(config.data_path):
    os.makedirs(config.data_path)

if __name__ == '__main__':
    c = Config
    print(c.BASE_URL)
