# 尚硅谷Linux笔记

## 1、基础

用户权限 rwx

```
umask:
    新建文件最大权限是666，没有执行权限；新建目录最大权限是7
    umask	直接查询；用户是002，root是022
umask运算：
	文件默认最大权限是666，umask的值是022
	用'-rw-rw-rw-' 减去 '-----w--w--w-' = '-rw--r--r--'	就是644
	目录最大权限777，umask 022
	'drwxrwxrwx' 减去 'd----w--w-' = 'drwxr-xr-x'	755
```

更改 所有者 所属组

```
chown user file	
chown user:usergroup file
chown user.usergroup file
chgrp usergroup file
```







## 2、命令

```
extundelete		误删除恢复
stat	显示文件或文件系统的状态
cat
less
more
man
	/字符串  当前页向下搜索
	?字符串  当前页想上搜索
	G 移动到行尾
	g移动到行首
	man -f 或 whatis 查看命令有哪几个级别帮助
	man -k 或 apropos commond 
info 
whereis	可以查找二进制命令，同时查找帮助文档
which	查找二进制命令，同时也可以查找命令别名
aliase
locate	查找，按照文件名称搜索文件
	文件数据库位置：/var/lib/mlocate/mlocate.db
	配置文件位置：/etc/updatedb.config
	locate dilename
	更新数据库：sudo updatedb
	配置文件：PRUNE_BIND_MOUNTS = "yes"	# 开启的搜索限制，配置文件生效
            PRUNEFS = ""	# 在搜索时，禁搜索这些系统了类类型文件
            PRUNENAMES = ""	# 禁止搜索带这些扩展名的文件
            PRUNAPATHS = "禁止搜索这些目录"
```

