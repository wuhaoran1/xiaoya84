import requests,pytest,json
from decimal import Decimal
from common.logger_handler import logger
from common.excel_handler import Exexl_handler
from common.mysql_handler import Mysql_handler
from config.path import cases_file
from config.yaml import host,member_id,exist_phone,exist_pwd,amount
data_login = Exexl_handler(cases_file).read("recharge")      #获取sheet页数据
@pytest.mark.parametrize("test_info",data_login)       #数据驱动
def test_recharge(test_info,login):
    url_acturl = host + test_info["url"]
    headers_acturl = json.loads(test_info["headers"])
    method_acturl = test_info["method"]
    json_acturl = test_info["json"]
    expected = test_info["expected"]
    if "#member_id#" in json_acturl:
        json_acturl = json_acturl.replace("#member_id#", str(member_id))
    headers_acturl["Authorization"] = login["token"]
    if "#wrong_member_id#" in json_acturl:
        json_acturl = json_acturl.replace("#wrong_member_id#",str(member_id + 1))
    if "#amount#" in json_acturl:
        json_acturl = json_acturl.replace("#amount#",str(amount))
    resp = requests.request(url=url_acturl,
                            headers=headers_acturl,
                            method=method_acturl,
                            json=json.loads(json_acturl))
    resp_body = resp.json()
    try:
        assert resp_body["code"] == expected  # 断言
    except AssertionError as err:
        logger.error("用例失败{}".format(err))  # 获取日志
        raise err  # 抛出异常
    if resp_body["code"] == 0:
        #数据库查询充值后的余额
        leave_amount_after = Mysql_handler().db\
            ("select leave_amount from futureloan.member where mobile_phone={} limit 10;".format(exist_phone))
        Mysql_handler().close()     #关闭游标、数据库连接
        #断言充值钱的余额 + 充值金额 = 充值后的余额
        assert Decimal(str(login["leave_amount"])) + Decimal(str(amount)) == Decimal(str(leave_amount_after[0]))
        
        