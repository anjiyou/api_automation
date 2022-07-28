import pytest
import requests
from common.yaml_util import YamlUtil


class TestProduct(object):
    @pytest.mark.parametrize("case_info",YamlUtil(r"./testcases/product_manage/get_file.yaml").read_yaml())
    def test_get_token(self,case_info):
        print(case_info)
        name = case_info["name"]
        method = case_info["request"]["method"]
        headers = case_info["request"]["headers"]
        url = case_info["request"]["url"]
        data = case_info["request"]["datas"]
        validate = case_info["validate"]
        response = requests.get(url=url,params=data,verify=False,timeout=10)
        result = response.text
        print(result)


