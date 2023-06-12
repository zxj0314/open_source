# Linux 查找命令

## locate 本地查找

```shell
locate	查找，按照文件名称搜索文件
	文件数据库位置：/var/lib/mlocate/mlocate.db
	配置文件位置：/etc/updatedb.config
	locate dilename
	更新数据库：sudo updatedb
	配置文件：PRUNE_BIND_MOUNTS = "yes"	# 开启的搜索限制，配置文件生效
            PRUNEFS = ""	# 在搜索时，禁搜索这些系统了类类型文件
            PRUNENAMES = ""	# 禁止搜索带这些扩展名的文件
            PRUNAPATHS = "禁止搜索这些目录"
命令参数：
    -b, --basename         匹配唯一的路径名称的基本文件名
    -c, --count            只显示找到条目的号码
    -d, --database DBPATH  用 DBPATH 替代默认的数据库(/var/lib/mlocate/mlocate.db)
    -e, --existing         只显示当前存在的文件条目
    -L, --follow           当文件存在时跟随蔓延的符号链接 (默认)
    -h, --help             显示本帮助
    -i, --ignore-case      匹配模式时忽略大小写区别
    -l, --limit, -n LIMIT  限制为 LIMIT项目的输出 (或 计数) 
    -m, --mmap             忽略向后兼容性
    -P, --nofollow, -H     当检查文件时不跟随蔓延的符号链接
    -0, --null             输出时以 NUL 分隔项目
    -S, --statistics       不搜索项目,显示有关每个已用数据库的统计信息
    -q, --quiet            不报告关于读取数据库的错误消息
    -r, --regexp REGEXP    搜索基本正则表达式 REGEXP 来代替模式
      --regex            模式是扩展正则表达式
    -s, --stdio            忽略向后兼容性
    -V, --version          显示版本信息
    -w, --wholename        匹配完整路径名 (默认)
```

## find 查找目录和文件

```shell
find ./ -name abc   # 在当前路径下查找 文件abc或目录
find ./ -iname abc   # 在当前路径下查找,忽略大小写
i节点查找：
    >>>ls -i abc
    >>>51924050 abc
    >>>find ./ -inum 51924050
    >>>./abc
find ./ -size 15c   # 查找15个字节的文件
按时间查找：
    -atime  [+|-]time   # 按照文件访问的时间搜索
    -mtime  [+|-]time   # 按照文件数据修改时间搜索
    -ctime  [+|-]time   # 按照文件状态修改时间搜索
    find ./ -mtime +5
按照权限搜索：
    find ./ -perm +644   # 只要三个权全部>=644就会被找到
    find ./ +perm +644   # 只要三个权限中包含一个644就会被找到
按照所有者、所属组、uid、gid、nouser
    -uid 用户id     # 按照用户id查找所有者是指定id的文件
    -gid 组id：     # 按照用户组id查找所属组是指定id的文件
    -user 用户名：  # 按照用户名查找所有者是指定用户的文件
    -group 组名：   # 按照组名查找所属组是指定用户组的文件
    -nouser：       # 查找没有所有者的文件
逻辑运算：
    -a      # and 逻辑与
    -o      # or 逻辑或
    -not    # not 逻辑非
    find ./ -name abc -a -type f
-exec
    find ./ -name abc -a -type f -exec ls -lh {} \;
-ok
    find ./ -name abc -a -type f -ok ls -lh {} \;
    find ./ -name abc -a -type f -ok rm -rf {} \;
    
    
参数说明：
    路径：告诉find在哪儿去找你要的东西，
    命令参数：参数很多下面会说到
    输出形式：输出形式很多，-print,-printf,-print0,-exec,-ok,-ls反正很多自己看手册吧。
    说一下exec，
    -exec find命令对匹配的文件执行该参数所给出的其他linux命令。相应命令的形式为' 命令 - and' {} \;，注意{ }和\；之间的空格。
    -ok 和- exec的作用相同，只不过和会人交互而已，OK执行前会向你确认是不是要执行。
find命令主要参数：
    -name 按照文件名查找文件。
    -perm 按照文件权限来查找文件。
    -prune 使用这一选项可以使find命令不在当前指定的目录中查找，如果同时使用了- depth选项，那么-prune选项将被find命令忽略。
    -user 按照文件属主来查找文件。
    -group 按照文件所属的组来查找文件。
    -mtime -n +n 按照文件的更改时间来查找文件， -n表示文件更改时间距现在n天以内，+n表示文件更改时间距现在n天以前。find命令还有-atime和-ctime选项，但它们都和-mtime选项
    相似，所以我们在这里只介绍-mtime选项。
    -nogroup 查找无有效所属组的文件，即该文件所属的组在/etc/groups中不存在。
    -nouser 查找无有效属主的文件，即该文件的属主在/etc/passwd中不存在。
    -newer file1 ! file2 查找更改时间比文件file1新但比文件file2旧的文件。
    -type 查找某一类型的文件，诸如：
    b - 块设备文件。
    d - 目录。
    c - 字符设备文件。
    p - 管道文件。
    l - 符号链接文件。
    f - 普通文件。
    s - socket文件
    -size n[cwbkMG] : 文件大小 为 n 个由后缀决定的数据块。其中后缀为：
    b: 代表 512 位元组的区块（如果用户没有指定后缀，则默认为 b）
    c: 表示字节数
    k: 表示 kilo bytes （1024字节）
    w: 字 （2字节）
    M:兆字节（1048576字节） 
    G: 千兆字节 （1073741824字节）
    -depth 在查找文件时，首先查找当前目录中的文件，然后再在其子目录中查找。
    -delete (删除)
    -maxdepth 查找最大目录层数 如 1，即只查找一层目录
    -iname 按名称搜索无论大小写
    -fstype 查找位于某一类型文件系统中的文件，这些文件系统类型通常可以在配置文件
    /etc/fstab中找到，该配置文件中包含了本系统中有关文件系统的信息。
    -mount 在查找文件时不跨越文件系统mount点。
    -follow(过时，新版使用-L)如果find命令遇到符号链接文件，就跟踪至链接所指向的文件。
    -cpio 对匹配的文件使用cpio命令，将这些文件备份到磁带设备中。
    -o 是或者的意思
    -a 是而且的意思
    -not 是相反的意思
    -empty 搜索空文件或空目录
    -xdev 确保find不回去遍历所有的文件系统，排除系统区域，只读源目录，可移动设备、/proc运行目录（linux系统）等类似位置
```