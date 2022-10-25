# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/21/2022 9:53 AM
# 文件名称: yaml_util.PY
import yaml
import os

#获取项目的根目录
def get_obj_path():
    return os.path.dirname(__file__).split('common')[0]

#读取yaml 需要安装pip install pyyaml
def read_yaml(yamlpath):
    with open(get_obj_path()+yamlpath,mode='r',encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value

#可以用该方法测试自己写的方法 D:\PycharmProjects\pytestDemo\common
if __name__ == '__main__':
    # print(read_yaml(r'\testcases\user_manage\get_token.yaml'))

    #结果 [{'name': '获取统一接口鉴权码', 'request': {'method': 'get', 'url': 'http://xxxx/token', 'data': {'grant_type': 'a', 'appid': 'v', 'secret': 'a'}}, 'validate': 'None'}]
    print(read_yaml(r'\testcases\user_manage\get_token2.yaml'))

