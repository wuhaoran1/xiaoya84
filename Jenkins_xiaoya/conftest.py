import pytest,requests
from pprint import pprint
from config.yaml import exist_phone
from jsonpath import jsonpath
@pytest.fixture()
def login():
    resp = requests.request(url="http://api.lemonban.com/futureloan/member/login",
                     method="post",
                     headers={"X-Lemonban-Media-Type":"lemonban.v2"},
                     json={"mobile_phone":exist_phone,"pwd":"12345678"})
    resp_body = resp.json()
    id = jsonpath(resp_body,"$..id")[0]
    leave_amount = jsonpath(resp_body,"$..leave_amount")[0]
    token_type = jsonpath(resp_body,"$...token_type")[0]
    token = jsonpath(resp_body,"$...token")[0]
    token = " ".join([token_type,token])
    return {"id":id,
            "leave_amount":leave_amount,
            "token":token}
if __name__ == '__main__':
    print(login())