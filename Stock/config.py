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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
        "Host": "xueqiu.com",
        "Cookie": "",
    }

    codes_list = os.path.join(BASE_URL, "data")


if __name__ == '__main__':
    c = Config
    print(c.BASE_URL)
