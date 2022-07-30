import os

import yaml

#获取项目根路径
def get_object_path():
    return os.getcwd()

#读取extract.yaml
def read_extract_yaml(yaml_path,key):
    with open(get_object_path() + "/" + yaml_path, mode="r", encoding="utf-8") as f:
        result = yaml.load(stream=f, Loader=yaml.FullLoader)
        return result[key]

#读取用例yaml
def read_testcase_yaml(yaml_path):
    with open(get_object_path() + "/" + yaml_path, mode="r", encoding="utf-8") as f:
        result = yaml.load(stream=f, Loader=yaml.FullLoader)
        return result


# 写入yaml文件
def write_yaml(yaml_path, data):
    with open(get_object_path() + "/" + yaml_path, mode="a", encoding="utf-8") as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)


# 清空yaml文件
def clean_yaml(yaml_path):
    with open(get_object_path() + "/" + yaml_path, mode="w", encoding="utf-8") as f:
        f.truncate()