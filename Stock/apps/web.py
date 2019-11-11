# -*- coding: utf-8 -*-


# @Time     : 19-11-10
# @Author   : Lattine

# =======================
from sanic import Sanic
from sanic.response import json
from config import ConfigXueQiu
from spiders.get_quotation import BaseInfo
from spiders.get_news import News

app = Sanic()


@app.route("/get_stock_quotation")
async def get_stock_quotation(request):
    cfg = ConfigXueQiu()
    bi = BaseInfo(config=cfg)
    bi.scrapy()
    return json({"msg": "get quotations success"})


@app.route("/get_stock_news")
async def get_stock_news(request):
    cfg = ConfigXueQiu()
    ns = News(config=cfg)
    ns.grap_news()
    return json({"msg": "get news success"})
