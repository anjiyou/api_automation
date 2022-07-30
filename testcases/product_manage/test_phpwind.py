"""
@Filename:testcases/product_manage/test_aaa
@Author:刘威
@Time:2022/7/30 14:02
@Describe:...
"""
import json
import re

import pytest

from commons.reuqest_util import RequestUtil
from commons.yaml_util import write_yaml, read_extract_yaml, read_testcase_yaml


class TestPhpwind(object):

    @pytest.mark.parametrize("case_info",read_testcase_yaml(r"testcases/product_manage/phpwind_index.yaml"))
    def test_index(self,case_info):
        name = case_info["name"]
        method = case_info["request"]["method"]
        url = case_info["request"]["url"]
        validate = case_info["validate"]
        res = RequestUtil().session.request(method=method,url=url)
        headers = dict(res.headers)
        data = {
            "csrf_token": re.search("csrf_token=(.+?);",json.dumps(headers)).group(1)
        }
        write_yaml("extract.yaml",data)

    @pytest.mark.parametrize("case_info",read_testcase_yaml(r"testcases/product_manage/phpwind_login.yaml"))
    def test_login(self,case_info):
        name = case_info["name"]
        method = case_info["request"]["method"]
        url = case_info["request"]["url"]
        headers = case_info["request"]["headers"]
        datas = case_info["request"]["datas"]
        datas["csrf_token"] = read_extract_yaml("extract.yaml","csrf_token")
        validate = case_info["validate"]
        res = RequestUtil().session.request(method=method,url=url,headers=headers,data=datas)
        result = res.json()
        print(result)