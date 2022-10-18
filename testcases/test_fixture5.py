# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/17/2022 8:55 AM
# 文件名称: test.PY
import pytest

class TestApi:

    def test_swh_api(self,um,db):
        #pass
        print("test  multi fixtures " + um + db)

