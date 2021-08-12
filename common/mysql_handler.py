import pymysql
class Mysql_handler:
    def __init__(self):
        self.con = pymysql.connect(host="8.129.91.152",    #连接数据库
                      port=3306,
                      user="future",
                      password="123456",
                      charset="utf8")
        self.curson = self.con.cursor()  # 获取游标
    def db(self,sql):
        self.curson.execute(sql)  # 通过游标执行sql
        data_db = self.curson.fetchone()  # 通过游标获取结果
        return data_db
    def close(self):
        self.curson.close()
        self.con.close()

if __name__ == '__main__':
    data = Mysql_handler().db("select mobile_phone from futureloan.member where mobile_phone=18362946935 limit 10;")
    Mysql_handler().close()
    print(type(data))
    print(type(data[0]))
    