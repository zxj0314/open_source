'''
os.getcwd() 方法用于返回当前工作目录。
os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
os.chdir() 方法用于改变当前工作目录到指定的路径。
os.mkdir() 方法用于以数字权限模式创建目录。默认的模式为 0777 (八进制)。
os.makedirs() 方法用于递归创建多层目录。
os.rmdir()方法用于删除指定路径的目录。
os.remove() 方法用于删除指定路径的文件。如果指定的路径是一个目录，将抛出OSError。
os.sep代表文件路径中的分隔符。
os.path.isdir() 方法用于检查指定的路径是否为现有目录。
os.path.isfile() 用于检查指定的路径是否是现有的常规文件。
os.path.split() 方法用于将路径名称拆分为一对头部和尾部
os.path.splitdrive() 方法用于将路径名称拆分为一对驱动器和尾部。
os.path.join() 方法会智能地连接一个或多个路径组件。
os.path.exists() 方法用于检查指定的路径是否存在。此方法还可用于检查给定的路径是否引用了打开的文件描述符。
os.path.abspath(path) 方法用于返回文件或者目录的绝对路径。
os.path.basename() 方法用于获取指定路径中的基本名称。
os.path.dirname() 方法用于从指定路径获取目录名称。
os.path.splitext() 方法用于将路径名分为成对的根和扩展名。
os.path.getsize(path) 返回文件大小，如果文件不存在就返回错误

'''

import os
import time

pathfile = "D:\Document\Python\Pytest_Workspace\Python基础\os_path.py"
path = "D:\Document\Python\Pytest_Workspace\Python基础"

# 判断
print(os.path.isabs(path))  # 是否为绝对路径
print(os.path.isdir(path))  # 是否为目录
print(os.path.isfile(pathfile))
print(os.path.islink("https://www.baidu.com"))
print(os.path.ismount(path))

# 获取路径操作
print(os.path.dirname(__file__))  # 获取当前路径 D:/Document/Python/Pytest_Workspace/Python基础
print(os.getcwd())  # 得到当前文件路径 D:\Git\gitee\open_source\Python_WorkSpace\Python_base\code
print(os.path.abspath(__file__))  # 获取当前文件的绝对路径

# 切割
# os.path.splitext() 方法用于将路径名分为成对的根和扩展名。
splitfilepath = os.path.split(pathfile)  # 将路径和文件名称分开
print(splitfilepath)
splitext = os.path.splitext("os_path.py")  # 将文件名称和扩展名分开
print(splitext)
splitdrive = os.path.splitdrive('D:\Git\gitee\open_source\Python_WorkSpace\Python_base\code')  # 将磁盘和路径分开
print(splitdrive)

# 获取文件名称
filename = pathfile[pathfile.rfind('\\') + 1:]
print(filename)
filename1 = os.path.split(pathfile)  # 文件分割，将路径和文件名分割；('D:\\Document\\Python\\Pytest_Workspace\\Python基础', 'os_path.py')
print(filename1)
print(filename1[1])

# 路径文件合并
file1 = os.path.join('D:\Git', 'os_path.py')  # 将路径和文件拼接在一起组成新的文件
print(file1)

# 遍历目录
all_file = os.listdir('../file')
print(all_file)

# 创建目录
if not os.path.exists('D:\\Git\\gitee\\open_source\\Python_WorkSpace\\Python_base\\file2'):
    print("#"*10)
    os.mkdir(r'D:\Git\gitee\open_source\Python_WorkSpace\Python_base\file2')
time.sleep(3)
# 删除目录
os.rmdir(r'D:\Git\gitee\open_source\Python_WorkSpace\Python_base\file2')

# 切换目录
print("切换前"+os.getcwd())
os.chdir("d:\git")
print("切换后"+os.getcwd())
