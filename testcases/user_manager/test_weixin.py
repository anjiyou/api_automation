import pytest

from commons.reuqest_util import RequestUtil
from commons.yaml_util import write_yaml, read_extract_yaml, read_testcase_yaml


class TestApi(object):
    @pytest.mark.parametrize("case_info",read_testcase_yaml(r"testcases/user_manager/get_token.yaml"))
    def test_get_token(self,case_info):
        name = case_info["name"]
        method = case_info["request"]["method"]
        url = case_info["request"]["url"]
        datas = case_info["request"]["datas"]
        validate = case_info["validate"]
        res = RequestUtil().send_all_request(method=method,url=url,params=datas)
        result = res.json()
        data = {
            "access_token":result["access_token"]
        }
        write_yaml("extract.yaml",data)
        TestApi.access_token = result["access_token"]
        print(type(result),result)

    @pytest.mark.parametrize("case_info",read_testcase_yaml(r"testcases/user_manager/get_tags.yaml"))
    def test_get_tag(self,case_info):
        name = case_info["name"]
        method = case_info["request"]["method"]
        url = case_info["request"]["url"]
        params = case_info["request"]["params"]
        params["access_token"] = read_extract_yaml("extract.yaml","access_token")
        validate = case_info["validate"]

        res = RequestUtil().send_all_request(method=method,url=url,params=params)
        result = res.json()
        print(type(result),result)

    @pytest.mark.parametrize("case_info",read_testcase_yaml(r"testcases/user_manager/create_tag.yaml"))
    def test_create_tag(self,case_info):
        name = case_info["name"]
        method = case_info["request"]["method"]
        url = case_info["request"]["url"]
        params = case_info["request"]["params"]
        params["access_token"] = read_extract_yaml("extract.yaml","access_token")
        datas = case_info["request"]["json"]
        validate = case_info["validate"]
        res = RequestUtil().send_all_request(method=method,url=url,params=params,json=datas)
        result = res.json()
        print(type(result),result)

    @pytest.mark.parametrize("case_info",read_testcase_yaml(r"testcases/user_manager/edit_tag.yaml"))
    def test_edit_tag(self,case_info):
        name = case_info["name"]
        method = case_info["request"]["method"]
        url = case_info["request"]["url"]
        params = case_info["request"]["params"]
        params["access_token"] = read_extract_yaml("extract.yaml", "access_token")
        datas = case_info["request"]["json"]
        validate = case_info["validate"]
        url = "https://api.weixin.qq.com/cgi-bin/tags/update"
        res = RequestUtil().send_all_request(method=method,url=url,params=params,json=datas)
        result = res.json()
        print(type(result),result)

    @pytest.mark.parametrize("case_info",read_testcase_yaml(r"testcases/user_manager/file_upload.yaml"))
    def test_file_upload(self,case_info):
        name = case_info["name"]
        method = case_info["request"]["method"]
        url = case_info["request"]["url"]
        params = case_info["request"]["params"]
        params["access_token"] = read_extract_yaml("extract.yaml", "access_token")
        datas = case_info["request"]["json"]
        datas["media"] = open("D:\\IDEA\\背景\\3.png",mode="rb")
        validate = case_info["validate"]
        res = RequestUtil().send_all_request(method=method,url=url,params=params,files=datas)
        result = res.json()
        print(type(result),result)

