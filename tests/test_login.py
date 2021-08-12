import requests,pytest
from common.logger_handler import logger
from common.excel_handler import Exexl_handler
from common.helper import number
from config.path import cases_file
from config.yaml import host,exist_phone,exist_pwd
data_login = Exexl_handler(cases_file).read("login")      #获取sheet页数据
@pytest.mark.parametrize("test_info",data_login)       #数据驱动
def test_login(test_info):
    url_acturl = host + test_info["url"]
    headers_acturl = test_info["headers"]
    method_acturl = test_info["method"]
    json_acturl = test_info["json"]
    expected = test_info["expected"]
    if "#new_phone#" in json_acturl:
         json_acturl = json_acturl.replace("#new_phone#",number)
    if "#exist_phone#" in json_acturl:
        json_acturl = json_acturl.replace("#exist_phone#",exist_phone)
    # if "#exist_pwd#" in json_acturl:
    #     json_acturl = json_acturl.replace("#exist_pwd#",exist_pwd)
    resp = requests.request(url=url_acturl,
                            headers=eval(headers_acturl),
                            method=method_acturl,
                            json=eval(json_acturl))
    resp_body = resp.json()
    try:
        assert resp_body["msg"] == expected  # 断言
    except AssertionError as err:
        logger.error("用例失败{}".format(err))  # 获取日志
        raise err  # 抛出异常
    