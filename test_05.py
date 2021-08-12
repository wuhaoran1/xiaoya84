import pymysql
from common.helper import number
con = pymysql.connect(host="8.129.91.152",    #连接数据库
                      port=3306,
                      user="future",
                      password="123456",
                      charset="utf8")
curson = con.cursor()    #获取游标
curson.execute("select * from futureloan.member where mobile_phone={} limit 10;".format(number))     #通过游标执行sql
data = curson.fetchone()      #通过游标获取结果
print(data)
curson.close()      #关闭游标
con.close()        #关闭数据库