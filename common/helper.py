from faker import Faker
from common.mysql_handler import Mysql_handler
def get_new_number():
    fk = Faker(locale="zh_CN")      #获取中文Faker
    while True:
        number = fk.phone_number()      #获取新号码
        data_in_mysql = Mysql_handler().db\
            ("select * from futureloan.member where mobile_phone={} limit 10;".format(number))    #查询数据库号码
        Mysql_handler().close()
        if not data_in_mysql:
            return number
number = get_new_number()
if __name__ == '__main__':
    print(get_new_number())
