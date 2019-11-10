# -*- coding: utf-8 -*-

# @Time    : 2019/11/10
# @Author  : Lattine

# ======================
from peewee import *

# 连接数据库
db = MySQLDatabase("stock", user="root", password="000000", host="localhost", port=3306)


class Stock(Model):
    code = CharField(max_length=20)  # 股票代码

    class Meta:
        database = db


class Quotation(Model):
    code = CharField(max_length=20)  # 股票代码
    name = CharField(max_length=50)  # 股票名称
    current_price = FloatField()  # 当前价格
    percent = FloatField()  # 当日涨幅
    amplitude = FloatField()  # 当日振幅
    turnover_rate = FloatField()  # 换手率
    date_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])  # 所属日期

    class Meta:
        database = db


class StockNews(Model):
    code = CharField(max_length=20)  # 股票代码
    title = CharField()  # 标题
    text = TextField()  # 内容
    date_at = DateTimeField()  # 所属日期

    class Meta:
        database = db


if __name__ == '__main__':
    try:
        db.create_tables([Stock, Quotation, StockNews])
        print("Tables is created.")
    except Exception as e:
        print(e)
