# -*- coding: utf-8 -*-

# @Time    : 2019/11/10
# @Author  : Lattine

# ======================
import time
import requests
from config import ConfigXueQiu
from dao.models import Stock, Quotation


class BaseInfo:
    def __init__(self, config):
        self.config = config
        self.codes = set()

        self._load_stocks()

    def scrapy(self):
        qts = self._get_quotations()
        sts = []
        for q in qts:
            if q["code"] not in self.codes:
                sts.append({"code": q["code"]})
                self.codes.add(q["code"])
        if sts:
            print(f"Stock table will update {len(sts)} items.")
            Stock.insert_many(sts).execute()
        Quotation.insert_many(qts).execute()
        print("stock's base info is update.")

    def _load_stocks(self):
        query = Stock.select()
        [self.codes.add(e.code) for e in query]

    def _get_quotations(self):
        qts = []
        for i in range(1, 1000):
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
            try:
                resp = requests.get(url=self.config.codes_hub, params=params, headers=self.config.headers)
                resp = resp.json()
                items = resp["data"]["list"]
                if len(items) == 0: break
                for item in items:
                    if item["turnover_rate"] is None:
                        continue
                    q = {
                        "code": item["symbol"],
                        "name": item["name"],
                        "current_price": item["current"],
                        "percent": item["percent"],
                        "amplitude": item["amplitude"],
                        "turnover_rate": item["turnover_rate"],
                    }
                    qts.append(q)
            except:
                continue
        return qts


if __name__ == '__main__':
    cfg = ConfigXueQiu()
    bi = BaseInfo(config=cfg)
    bi.scrapy()
