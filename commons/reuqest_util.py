"""
@Filename:commons/reuqest_util
@Author:刘威
@Time:2022/7/30 16:21
@Describe:...
"""
import requests


class RequestUtil(object):
    session = requests.Session()

    def send_all_request(self,method,url,**kwargs):
        response = RequestUtil.session.request(method=method,url=url,**kwargs)
        return response