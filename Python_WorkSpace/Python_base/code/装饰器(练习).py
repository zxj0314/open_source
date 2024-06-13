# 装饰器登录练习
import time

isLogin = False


def login():
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username == "admin" and password == "123456":
        print("已登录，允许付款")
        return True
    else:
        return False


def LoginRequired(func):
    def wapper(*args, **kwargs):
        global isLogin
        print("登录校验")
        if isLogin:
            func(*args, **kwargs)
        else:
            print("用户名登陆不能付款")
            isLogin = login()
            print("是否登录成功", isLogin)

    return wapper


@LoginRequired
def pay(money):
    print("---------购买商品---------")
    print("付款中…………")
    time.sleep(2)
    print("付款{}完成".format(money))


pay(100)

pay(100)
