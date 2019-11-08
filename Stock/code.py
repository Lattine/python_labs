# -*- coding: utf-8 -*-

# @Time    : 2019/11/4
# @Author  : Lattine

# ======================
import os
import re
import json
import requests
import time
import datetime
from config import Config
from api import get_html
from html import MainContent


class SHSZ:
    def __init__(self, config):
        self.config = config  # 配置
        self.week_day = datetime.datetime.now().weekday()  # 判读当天周几，不同的时间有不同的操作
        self.time_thresh = 86400 if self.week_day != 1 else 259200  # 周一需要爬取3天的新闻

        self.mc = MainContent()  # HTML内容抽取类

        if self.week_day in [1, 2, 3, 4, 5]:  # 只有工作日的信息才需要爬取
            self.codes = self._grap_codes()  # 获取所有股票代码
            self._grap_news()
            self._dump_codes()
        else:
            print("Sat. and Sun. Day should passed!")

    def _grap_codes(self):
        datas = []
        for i in range(1, 1000):
            try:
                params = {
                    "page": i,
                    "size": 100,
                    "order": "asc",
                    "orderby": "code",
                    "order_by": "symbol",
                    "market": "CN",
                    "type": "sh_sz",
                    "_": int(time.time() * 1000)
                }
                resp = requests.get(url=self.config.codes_hub, params=params, headers=self.config.headers)
                resp = resp.json()
                items = resp["data"]["list"]
                if len(items) == 0: break
                for item in items:
                    em = {
                        "code": item["symbol"],
                        "name": item["name"],
                        "current_price": item["current"],
                        "percent": item["percent"],
                        "amplitude": item["amplitude"],
                        "turnover_rate": item["turnover_rate"],
                    }
                    datas.append(em)
            except:
                continue
        return datas

    def _grap_news(self):
        for item in self.codes:
            print(item["code"])
            item["news"] = self._grap_news_by_code(item["code"])

    def _grap_news_by_code(self, code):
        news = []
        try:
            params = {
                "symbol_id": code,
                "count": 20,
                "source": "自选股新闻",
                "page": 1
            }
            resp = requests.get(self.config.news_hub, params=params, headers=self.config.headers)
            resp = resp.json()

            items = resp["list"]
            for item in items:
                if time.time() - item["created_at"] / 1000 < 24 * 60 * 60:
                    url = re.findall(r"href=\"(.*?)\" ", item["text"])[0]  # 获取新闻URL
                    status, html = get_html(url)
                    if status:
                        title, content = self.mc.extract(url, html)
                    news.append({"time": item["created_at"] / 1000, "title": title, "content": content})
        except:
            pass
        return news

    def _dump_codes(self):
        now = datetime.datetime.now()
        today = datetime.datetime.strftime(now, r"%Y-%m-%d")
        with open(os.path.join(self.config.data_path, "{}.json".format(today)), "w+", encoding="utf-8") as fw:
            json.dump(self.codes, fw, ensure_ascii=False, indent=True)


if __name__ == '__main__':
    config = Config()
    p = SHSZ(config)