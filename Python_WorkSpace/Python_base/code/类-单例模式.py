# 创建单例模式
# 只创建一个内存空间，

class Singletion:
    # 私有化变量，确认是否创建内存空间
    __instance = None

    # 重写new，创建对象只生成一次地址
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        #     return cls.__instance
        # else:
        #     return cls.__instance
        return cls.__instance


s1 = Singletion()
print(s1)
s2 = Singletion()
print(s2)
