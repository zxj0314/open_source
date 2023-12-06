# 本地与linux互传文件方式

## 1、 lrzsz

*   安装：    `yum -y install lrzsz`
*   rpm检查是否正确安装：   `rpm =qa lrzsz`
*   上传：`rz 或 rz -be`
*   下载：`sz file`

## 2 scp (linux 间通信)

*   上传到服务器

```shell
scp 本地文件路径+文件名 远程主机用户名@ip:需要上传到远程主机的路径
scp -r 本地文件路径+文件夹名 远程主机用户名@ip:需要上传到远程主机的路径
例：
scp /Users/pc/Desktop/test.png root@192.168.1.1:/root
scp -r /Users/pc/Desktop/test root@192.168.1.1:/root
```

*   下载到本地

```shell
scp 远程主机用户名@ip:服务器上存放文件的路径  下载到本地的文件路径
scp -r 远程主机用户名@ip:服务器上存放文件的路径  下载到本地的文件路径
例：
scp root@192.168.1.1:/root/test.png /Users/pc/Desktop
scp -r root@192.168.1.1:/root/test /Users/mac/Desktop
```

## **3、 sftp**
`sftp username\@ip   *//sftp 用户名@服务器IP地址* `
* 上传：
```shell
lpwd：显示本地路径
pwd：显示远程路径
例：
put  D:/test.txt  /home/test/
或：
sftp> lcd D:/
sftp> cd /home/test
sftp> put text.txt
把本地的D:/目录下面的text.txt文件上传到远程服务器的/home/test目录下

```
* 下载
```shell
get 远程路径/文件名 本地路径
get -r 远程路径/文件名 本地路径
sftp> cd /home/test
sftp> lcd D:/test
sftp> get -r log
把远程服务器的/home/test目录下面的log文件夹下载到本地服务器的D:/test目录下
```
## 4、xftp软件
输入名称，主机地址，选择sftp协议，端口22，用户名和密码连接。