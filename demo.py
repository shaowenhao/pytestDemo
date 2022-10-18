# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/9/2022 7:08 PM
# 文件名称: demo.PY

# ctrl + q 快速查看文档
import requests
import sys

response = requests.get("https://baidu.com")
print(response.text)

print(sys.argv[1])