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
        self.config = config
        self.mc = MainContent()
        self.codes = self._grap_codes()
        self._grap_news()
        self._dump_codes()

    def _grap_codes(self):
        datas = []
        for i in range(1, 2):
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
                break
        return datas

    def _grap_news(self):
        for item in self.codes:
            item["news"] = self._grap_news_by_code(item["code"])
            break

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
            print(resp, resp.url)
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
        print(today)
        with open(os.path.join(self.config.data_path, "{}.json".format(today)), "w+", encoding="utf-8") as fw:
            json.dump(self.codes, fw, ensure_ascii=False, indent=True)


if __name__ == '__main__':
    config = Config()
    p = SHSZ(config)
