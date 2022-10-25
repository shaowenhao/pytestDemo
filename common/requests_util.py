# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/24/2022 4:14 PM
# 文件名称: requests_util.PY
import requests as requests


class RequestUtil:
    session = requests.session()

    def send_request(self,method,url,data,**kwargs):
        method = str(method).lower()
        res = ""
        if method == "get":
            res = RequestUtil.session.request(method,url,params=data,**kwargs)
        elif method == "post":
            res = RequestUtil.session.request(method,url,json=data,**kwargs)
        return res
