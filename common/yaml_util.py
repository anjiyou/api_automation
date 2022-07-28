import yaml

class YamlUtil(object):
    def __init__(self,yaml_path):
        self.yaml_path = yaml_path

    #读取yaml文件
    def read_yaml(self):
        with open(self.yaml_path,mode="r",encoding="utf-8") as f:
            result = yaml.load(stream=f,Loader=yaml.FullLoader)
            return result

    #写入yaml文件
    def write_yaml(self,data):
        with open(self.yaml_path,mode="w",encoding="utf-8") as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)

    #清空yaml文件
    def clean_yaml(self):
        with open(self.yaml_path,mode="w",encoding="utf-8") as f:
            f.truncate()

if __name__ == '__main__':
    yaml_util = YamlUtil(r"../testcases/product_manage/get_token.yaml")
    result = yaml_util.read_yaml()
    print(result,type(result))