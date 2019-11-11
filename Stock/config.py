# -*- coding: utf-8 -*-

# @Time    : 2019/11/4
# @Author  : Lattine

# ======================
import os


# 加载cookie
def load_cookies(path):
    cookies = []
    with open(path, encoding="utf-8") as fr:
        for line in fr:
            cookies.append(line.strip())
    return cookies


class ConfigXueQiu:
    BASE_URL = os.path.abspath(os.getcwd())

    codes_hub = "https://xueqiu.com/service/v5/stock/screener/quote/list"
    news_hub = "https://xueqiu.com/statuses/stock_timeline.json"
    headers = {
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'xueqiu.com',
        'Referer': 'https://xueqiu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    xueqiu_cookie_file = os.path.join(BASE_URL, "data", "cookie_xueqiu.txt")
    xueqiu_cookies = load_cookies(xueqiu_cookie_file)
    data_path = os.path.join(BASE_URL, "data")
