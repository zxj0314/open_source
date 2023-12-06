# pip详解
pip 是 Python 的包管理工具，我们常使用 pip 命令来安装和卸载 Python 的第三方库。
## # Linux下安装pip

```python
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   # 下载安装脚本
$ sudo python get-pip.py    # 运行安装脚本
```
## 2. 使用 pip 安装 python 第三方库
```python
pip install requests        # 安装 requests 第三方库
pip install xlrd==1.2.0     # pip 安装 xlrd 的 1.2.0版本
pip uninstall xlrd         # 使用 pip 卸载第三方库 xlrd
pip list        # pip 查看已经安装的第三方库
```

## 3、pip 常用命令

```
pip --version  # 显示版本和路径
pip --help  #获取帮助
pip install -U pip #升级pip
pip install SomePackage #最新版本
pip install SomePackage==1.0.4 #指定版本
pip install SomePackage>=1.0.4 #最小版本
pip install --upgrade SomePackage #升级包，通过使用==，>=, <=, >, < 来指定一个版本号
或 pip install -U SomePackage #升级包
pip uninstall SomePackage #卸载包
pip search SomePackage #搜索包
pip show #显示安装包的信息
pip show -f SomePackage #查看指定包的详细信息
pip list #列出已安装的包
pip list -o #查看可升级的包
pip freeze #查看已经安装的包以及版本信息
pip freeze -r requirements.txt    # 到处所有安装包版本
pip install -r requirements.txt #安装指定文件中的包
```

## 4、pip 使用国内镜像源

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simplele reques
# 永久更换下载源
linux下： ~/.pip/pip.conf
    [global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
# windows用户:
直接在user目录中创建一个pip目录，如：C:\Users\xx\pip；在pip 目录下新建文件pip.ini
    [global] 
    timeout = 6000 
    index-url = https://pypi.tuna.tsinghua.edu.cn/simplel
    trusted-host = pypi.tuna.tsinghua.edu.cn
常用镜像源网址
    清华：https://pypi.tuna.tsinghua.edu.cn/simple
    阿里云：http://mirrors.aliyun.com/pypi/simple/
    中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
    豆瓣：http://pypi.douban.com/simple/
查看 镜像地址：
$ pip3 config list
    global.index-url='https://pypi.tuna.tsinghua.edu.cn/simple'
    install.trusted-host='https://pypi.tuna.tsinghua.edu.cn'
```
