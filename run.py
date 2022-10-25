# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/10/2022 9:34 PM
# 文件名称: run.PY
import os
import time

import pytest

# 配置了pytest.ini指定了addopts 这里可以不用配
if __name__ == '__main__':
    pytest.main()
    time.sleep(5)

    os.system("allure generate ./temp -o ./reports --clean")
# 这里不加参数 但是再ini的配置文件中有