# tests 放置测试用例
# reports  放置测试报告
# data  放置测试数据
# run.py 主程序，收集用例，运行用例，收集报告
# conftest.py的作用范围
一个工程下可以建多个conftest.py的文件，一般在工程根目录下设置的conftest文件起到全局作用。
在不同子目录下也可以放conftest.py的文件，作用范围只能在改层级以及以下目录生效。
    1.conftest在不同的层级间的作用域不一样
    2.conftest是不能跨模块调用的（这里没有使用模块调用）
# 充值
member_id， 需要登陆接口返回
登录接口的作用：
   得到id
   得到token
   得到leave_amount
充值接口依赖于登录这个接口登录是不是就是充值的前置条件??
使用pytest当中的fixture夹具实现前置条件。

    检验：
        校验接口的返回信息， msg， code是否正常
    充值成功；
          余额是否正确，充值之前的余额+充值的钱==充值之后的余额
# 接口需要的member_id，三种方式
    写死在excel， 麻烦
    写在配置文件，
    登录接口获取
