import pytest
# def login(username,password):
#     if username == 1 and password == 2:
#         return "成功"
#     return "失败"
# data = [{"u":1,"p":2,"excepted":"成功1"},
#         {"u":"","p":"","excepted":"失败"}]
# @pytest.mark.parametrize("test_info",data)
# def test_login(test_info):
#     u = test_info["u"]
#     p = test_info["p"]
#     excepted = test_info["excepted"]
#     assert excepted == login(u,p)
# import pytest
# @pytest.fixture()
# def add():
#     return 1
# def test_one(add):
#     print("wode",add)
#     assert 2 == add
import json
m = '{"aa":1,"bb":2}'
# mm = eval(m)
# print(mm)
x = json.loads(m)
print(x)
