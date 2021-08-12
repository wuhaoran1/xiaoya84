# class Car:
#     one = 111
#     two = 222
#     def __init__(self,logo=111,color=222):
#         self.logo = logo
#         self.color = color
#     def driver(self,distance=100):
#         print("距离{}公里".format(distance))
#
#         self.distance = distance
#         return "222231"
#     def add(self):
#         print("123{}".format(self.distance))
# my_Car = Car()
# print(my_Car.logo)
# print(my_Car.driver())
# my_Car.add()
# a = "11"
# b = "22"
# from jsonpath import jsonpath
# data = {
#     "code": 0,
#     "msg": "OK",
#     "data": {
#         "id": 123508026,
#         "leave_amount": 0,
#         "mobile_phone": "18362946935",
#         "reg_name": "542",
#         "reg_time": "2021-08-08 21:32:38.0",
#         "type": 1,
#         "token_info": {
#             "token_type": "Bearer",
#             "expires_in": "2021-08-09 11:53:41",
#             "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEyMzUwODAyNiwiZXhwIjoxNjI4NDgxMjIxfQ.h2CNXimO1Q4sD6ttkcwiTELLVQqX8i8nN8t0Q7GRlTc5QpqzTHQ5ox1WnllzEENncvXQM3iB167-gKN1GL0L6A"
#         }
#     },
#     "copyright": "Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"
# }
# aa = jsonpath(data,"$...token")[0]
# print(aa)
# a = '{"aa":"x","bb":22}'
# b = a.replace("x","22")
# print(b)
a = (1,2)
print(type(a[0]))
