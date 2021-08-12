import requests
import pytest
from common.logger_handler import logger       #导入logger
from common.excel_handler import Exexl_handler
from config.path import cases_file
from config.yaml import host,exist_phone
from common.helper import number
data_register = Exexl_handler(cases_file).read("register")      #获取sheet页数据
@pytest.mark.parametrize("test_info",data_register)       #数据驱动
def test_register(test_info):
    url_acturl = host+ test_info["url"]
    headers_acturl = test_info["headers"]
    method_acturl = test_info["method"]
    json_acturl = test_info["json"]
    expected = test_info["expected"]
    if "#exist_phone#" in json_acturl:
        json = json_acturl.replace("#exist_phone#",exist_phone)
    if "#new_phone#" in json_acturl:
        json_acturl = json_acturl.replace("#new_phone#",number)
    resp = requests.request(url=url_acturl,    #url
                            headers=eval(headers_acturl),      #请求头
                            method=method_acturl,      #方法
                            json=eval(json_acturl))         #请求体

    resp_body = resp.json()
    try:
        assert resp_body["code"] == expected      #断言
    except AssertionError as err:
        logger.error("用例失败{}".format(err))      #获取日志
        raise err       #抛出异常
    