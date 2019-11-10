# -*- coding: utf-8 -*-

# @Time    : 2019/11/4
# @Author  : Lattine

# ======================
import cchardet
import requests


def get_html(url, timeout=10, headers=None):
    _headers = {
        "User-Agent": 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
    }
    if headers:
        _headers = headers
    try:
        r = requests.get(url, headers=_headers, timeout=timeout)
        encoding = cchardet.detect(r.content)["encoding"]
        html = r.content.decode(encoding)
        status = r.status_code
    except:
        html = ""
        status = 0
    return status, html
