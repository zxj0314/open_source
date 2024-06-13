'''
基本的异常处理：try/except
在Python中，所有的异常都继承自BaseException类。
异常处理的其他语句：finally 和 else
    - finally语句块中的代码无论是否发生异常都会被执行。
    - else语句块中的代码会在try块没有抛出任何异常的情况下运行。
抛出异常：raise
    class MyException(Exception):
        pass
    raise MyException('An exception of type MyException occurred')
    raise MyCustomException('An error occurred') from e  # 异常链接
捕获多个异常
    except (ValueError, TypeError):
获取异常信息
    在except语句中，你可以将异常对象赋值给一个变量，并利用这个变量来获取异常信息。
    except Exception as e:
    print('Caught an exception:', type(e), e)
'''


# 自定义异常
class MyCustomException(BaseException):
    pass
    raise FileNotFoundError('An exception of type MyCustomException occurred')


try:
    x = 1 / 0
except ZeroDivisionError:
    print('Caught a ZeroDivisionError')
except TypeError:
    print('Caught a TypeError')
except (ValueError, TypeError):
    print('Caught a TypeError TypeError')

except Exception as e:
    raise MyCustomException('An error occurred') from e  # 异常链接
