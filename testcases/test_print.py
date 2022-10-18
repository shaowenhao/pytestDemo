# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/10/2022 8:12 PM
# 文件名称: test_print.PY
import time

import pytest

from common.common_util import CommonUtil


class TestPrint(CommonUtil):


    workage = 8


# add @pytest.mark.smoke to mark this case as smoke
    @pytest.mark.smoke
    def test_print1(self):
        time.sleep(3)
        print("测试打印功能")
        #raise Exception("self defined except")

    @pytest.mark.skip(reason = "no reason skip")
    def test_print2(self):
        time.sleep(3)
        print("测试打印功能2")

    @pytest.mark.skipif(workage < 10, reason="work experience not long")
    def test_print3(self):
        time.sleep(3)
        print("测试打印功能3")
# 正常的写法不会直接在这里写main
# if __name__ == '__main__':
#     pytest.main()
