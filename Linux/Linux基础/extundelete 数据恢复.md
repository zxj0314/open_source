# Linux下rm误删恢复 extundelete
误删之后要第一时间卸载（umount）该分区，或者以只读的方式来挂载（mount）该分区，否则覆写了谁也没办法恢复。如果误删除的是根分区，最好直接断电，进入单用户模式，以只读的方式挂在分区，然后再进行恢复。

## 1、安装
整体安装步骤
```shell
# 源码下载
wget https://nchc.dl.sourceforge.net/project/extundelete/extundelete/0.2.4/extundelete-0.2.4.tar.bz2
# 解压
tar -jxvf extundelete-0.2.4.tar.bz2
# 进入目录并编译安装
cd extundelete-0.2.4
./configure
sudo make && make install
```

如果上面这几步都完美运行没有报错并得到类似以下的输出那么安装就顺利成功了，下面的报错总结即可跳过。
```
cd src
extundelete -v
```
输出：
```
extundelete version 0.2.4
libext2fs version 1.44.1
Processor is little endian.
```
执行make命令会在src目录下生成 extundelete 可执行文件，可在此直接执行恢复命令， 执行 make install 会将程序安装在 /usr/local/bin/ 下。

## 2、安装报错总结
### 2.1 编译配置时报错
如果在编译配置 ./configure 时报错：
```
$ ./configure
Configuring extundelete 0.2.4
configure: error: Can't find ext2fs library
```
说明确是 ext2fs 库，直接安装即可：
`sudo apt-get install e2fslibs-dev e2fslibs-dev`

配置这一步成功的话正常输出应为：
```
$ ./configure
Configuring extundelete 0.2.4
Writing generated files to disk
```

### 2.2 编译时报错
如果在编译 make 时报错：
```
$ make && make install
make -s all-recursive
Making all in src
insertionops.cc: In function ‘std::ostream& operator<<(std::ostream&, const ext2_inode&)’:
insertionops.cc:36:36: error: ‘const struct ext2_inode’ has no member named ‘i_dir_acl’; did you mean ‘i_file_acl’?
   os << "Directory ACL: " << inode.i_dir_acl << std::endl;
                                    ^~~~~~~~~
                                    i_file_acl
Makefile:437: recipe for target 'extundelete-insertionops.o' failed
make[2]: *** [extundelete-insertionops.o] Error 1
Makefile:268: recipe for target 'all-recursive' failed
make[1]: *** [all-recursive] Error 1
Makefile:208: recipe for target 'all' failed
make: *** [all] Error 2
```
需要打一个补丁：
```
wget https://sourceforge.net/p/extundelete/tickets/5/attachment/extundelete-0.2.4-e2fsprogs.patch.txt
patch -p1<extundelete-0.2.4-e2fsprogs.patch.txt
./configure
sudo make && make install
```
## 3、恢复误删文件
所有的 extundelete 的命令可以通过 extundelete --help 来查看，这里介绍几个常用的。

* 查看要恢复的文件的分区并卸载
```
df -Th
sudo umount /media
```
* 查看可以恢复的数据
```
sudo extundelete /dev/sda --inode 2 
是分区根目录的 inode 值。
```
* 恢复单个目录
指定要恢复的目录名，如果是空目录，则不会恢复。
`extundelete /dev/sda --restore-directory  tbx/`
当执行恢复文件的命令后，会在执行命令的当前的目录下生成 RECOVERED_FILES 目录，恢复的文件都会放入此目录中。如未生成目录，即为失败。

* 恢复单个文件
指定要恢复的文件名，如果几k大小的小文件，有很大几率恢复失败。
`sudo extundelete /dev/sda --restore-file openssh-7.7p1.tar.gz`

* 恢复删除的全部文件
无需指定文件名或目录名，恢复全部删除的数据。
`sudo extundelete /dev/sda --restore-all `
