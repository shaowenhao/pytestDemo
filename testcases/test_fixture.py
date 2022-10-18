# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/17/2022 8:55 AM
# 文件名称: test.PY
import pytest


@pytest.fixture(scope="function",autouse=True)
def exe_database_sql():
    print("execute sql")
    yield
    print("close db connection")

class TestFixture:

    def test_swh(self):
        print("test fixture 11")

# 这样做就可以让想要的case执行前置的步骤
# def test_swh2(self,exe_database_sql):
    def test_swh2(self):
        print("test fixture 22")