# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/15/2022 4:53 PM
# 文件名称: common_util.PY

class CommonUtil:
    def setup_class(self):
        print("before class")

    def teardown_class(self):
        print("after class")

    def setup(self):
        print("before each test case")

    def teardown(self):
        print("after each test case")