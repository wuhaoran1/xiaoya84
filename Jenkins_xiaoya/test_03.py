# from review.demo_定制日志等级封装类 import Get_logger
# log = Get_logger(file="review.log")
import logging
def test_add():
    c = 6
    expected = 7
    # try:
    #     assert c == expected
    # except AssertionError as err:
    #     logging.error("报错{}".format(err))     #报错信息
    assert c == expected

# if __name__ == '__main__':
#     add(2,4)
