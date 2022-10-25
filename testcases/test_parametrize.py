# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/19/2022 6:47 PM
# 文件名称: test_parametrize.PY
import pytest

from common.common_util import CommonUtil


class TestParam(CommonUtil):

    # @pytest.mark.parametrize('caseinfo',['python','java','c#'])
    # def test_get_token(self,caseinfo):
    #     print("获取统一接口鉴权码" + caseinfo)

    # 获取统一接口鉴权码nameshaowenhao 这是一种解包

    # @pytest.mark.parametrize('arg1,arg2', [['name', 'shaowenhao'], ['age', '18']])
    # def test_get_token(self, arg1, arg2):
    #     print("获取统一接口鉴权码" + str(arg1) + str(arg2))

    # 获取统一接口鉴权码['age', '18']
    @pytest.mark.parametrize('arg', [['name', 'shaowenhao'], ['age', '18']])
    def test_get_token(self, arg):
        print("获取统一接口鉴权码" + str(arg))
