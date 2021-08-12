import requests
import logging
def test_register():
    url = "http://api.lemonban.com/futureloan/member/login"
    headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
    method = "post"
    json = {"mobile_phone":"18806212504","pwd":"12345678"}
    expected = 1
    resp = requests.request(url=url,    #url
                            headers=headers,      #请求头
                            method=method,      #方法
                            json=json)         #请求体
    resp_body = resp.json()
    try:
        assert resp_body["code"] == expected
    except AssertionError as err:
        logging.error("用例失败{}".format(err))
        raise err