# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/17/2022 2:35 PM
# 文件名称: conftest.PY
import pytest

def read_yaml():
    return ['shaowenhao','duxiaodan','shaojunheng']

@pytest.fixture(scope="function",autouse=False,params=read_yaml(),name="db")
def exe_database_sql(request):
#   print(request.param)
    print("query 221017")
    yield request.param
    print("close 221017")

@pytest.fixture(scope="function",autouse=False,name="um")
def user_manage(request):
#   print(request.param)
    print("user manage module work in prepare")
    yield "user_manage"
    print("user manage module work after finish")
