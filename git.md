### 命令行指引

你还可以按照以下说明从计算机中上传现有文件。

##### Git 全局设置

```
git config --global user.name "宝石杰"
git config --global user.email "zxj@outlook.com"
```

创建私钥

```
ssh-keygen -t rsa -b 2048 -C "zxj@outlook.com" 
```

##### 创建一个新仓库

```
git clone https://gitcode.net/qq_42184753/open_source.git
cd open_source
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```

##### 推送现有文件夹

```
cd existing_folder
git init
git remote add origin https://gitcode.net/qq_42184753/open_source.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

**推送现有的 Git 仓库`cd existing_repo**

```
git remote rename origin old-origin
git remote add origin https://gitcode.net/qq_42184753/open_source.git
git push -u origin --all
git push -u origin --tags
```

