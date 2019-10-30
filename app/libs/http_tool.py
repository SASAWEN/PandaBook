"""
    Created by cala at 2019-10-25
"""
# -*- coding:utf-8 -*-
import requests

# 获取http请求
# urllib 自带
# requests 三方库
class HTTP:
    # return_json 是否返回json格式请求
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code == 200:
            if return_json:
                print(r.json())
            return r.json() if return_json else r.text
        return {} if return_json else ''


