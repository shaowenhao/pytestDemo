# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/19/2022 6:47 PM
# 文件名称: test_parametrize.PY
import pytest
import requests as requests

from common.common_util import CommonUtil
from common.requests_util import RequestUtil
from common.yaml_util import read_yaml


class TestParam(CommonUtil):

    # @pytest.mark.parametrize('caseinfo',['python','java','c#'])
    # def test_get_token(self,caseinfo):
    #     print("获取统一接口鉴权码" + caseinfo)

    # 获取统一接口鉴权码nameshaowenhao 这是一种解包

    # @pytest.mark.parametrize('arg1,arg2', [['name', 'shaowenhao'], ['age', '18']])
    # def test_get_token(self, arg1, arg2):
    #     print("获取统一接口鉴权码" + str(arg1) + str(arg2))

    # 获取统一接口鉴权码['age', '18']

    # 刚开始先把session加载这里 只是为了跑通case，实际上会在common里加util工具类
    # session = requests.Session()
    access_token = ""

    @pytest.mark.parametrize('caseinfo', read_yaml(r'\testcases\user_manage\get_token2.yaml'))
    def test_get_token(self, caseinfo):
        print("获取统一接口鉴权码的参数：" + str(caseinfo))
        # 单条case返回的字典 字典的查询
        print(caseinfo['name'])
        print(caseinfo['request']['method'])
        print(caseinfo['request']['url'])

        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        #params get, json dta post
        rsp = RequestUtil.session.request(method=method, url=url, params=data)
        print(rsp.json())

        result = rsp.json()
        assert 'access token' in result
        TestParam.access_token = rsp.json()['access_token']
    # 获取统一接口鉴权码的参数：{'name': '获取统一接口鉴权码', 'request': {'method': 'get', 'url': 'http://xxxx/token', 'data': {'grant_type': 'a', 'appid': 'v', 'secret': 'a'}}, 'validate': 'None'}


    # 接口关联
    @pytest.mark.parametrize('caseinfo', read_yaml(r'\testcases\user_manage\edit_flag.yaml'))
    def test_02_edit_flag(self, caseinfo):
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url'] + TestParam.access_token
        data = caseinfo['request']['data']
        #因为case里传入的数据是 jason格式的，如果是表单 可以用 data=xxx
        rsp = RequestUtil.session.request(method=method, url=url, json=data)
        print(rsp.json())

