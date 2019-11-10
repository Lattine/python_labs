# -*- coding: utf-8 -*-

# @Time    : 2019/11/10
# @Author  : Lattine

# ======================
import re
import time
import datetime
import random
import requests

from config import ConfigXueQiu
from dao.models import Stock, StockNews
from spiders.html.parse_content import MainContent
from spiders.api.downloader import get_html


class News:
    def __init__(self, config):
        self.config = config
        self.codes = set()

        self.week_day = datetime.datetime.now().weekday()  # 判读当天周几，不同的时间有不同的操作
        self.time_thresh = 86400 if self.week_day != 1 else 259200  # 周一需要爬取3天的新闻

        self.mc = MainContent()  # HTML内容抽取类

        if self.week_day in [1, 2, 3, 4, 5, 6, 0]:  # 只有工作日的信息才需要爬取
            self._load_stocks()  # 获取所有股票代码
        else:
            print("Sat. and Sun. Day should passed!")

    def grap_news(self):
        news = []
        for code in self.codes:
            self.config.headers["cookie"] = random.choice(self.config.xueqiu_cookies)
            temp_news = self._grap_news_by_code(code)
            news.extend(temp_news)

        StockNews.insert_many(news).execute()

    def _grap_news_by_code(self, code):
        news = []
        params = {
            "symbol_id": code,
            "count": 20,
            "source": "自选股新闻",
            "page": 1
        }
        try:
            resp = requests.get(self.config.news_hub, params=params, headers=self.config.headers, verify=False)
            resp = resp.json()
            items = resp["list"]
            for item in items:
                self._crawl_single_news(news, item, code)
        except:
            pass
        return news

    def _crawl_single_news(self, news, item, code):
        news_at = item["created_at"] / 1000
        if time.time() - news_at < self.time_thresh:
            url = re.findall(r"href=\"(.*?)\" ", item["text"])[0]  # 获取新闻URL
            status, html = get_html(url)
            if status:
                title, content = self.mc.extract(url, html)
                news.append({"code": code,
                             "title": title,
                             "text": content,
                             "date_at": datetime.datetime.fromtimestamp(news_at)})

    def _load_stocks(self):
        query = Stock.select()
        [self.codes.add(e.code) for e in query]


if __name__ == '__main__':
    cfg = ConfigXueQiu()
    ns = News(config=cfg)
    ns.grap_news()
