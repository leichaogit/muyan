使用github或者码云进行代码托管

```
创建git仓库
gitinit【用命令行进入当前的环境中，在进行创建】
工作区
git add . 【将工作区的全部内容提交到暂存区】
git status 【查看工作区状态】
暂存区
git commit -m '描述信息' 【将暂存区内容添加到本地仓库】
本地仓库
设置全局用户名 :git config userneme 'xx'
设置全局邮件邮箱:git config useremail 'xxx'
git push 【将内容添加到远程仓库】
远程仓库
1.gitbub或者码云
```

```
远程仓库使用注意
1、取消勾选自动生成readme文件:勾选会产生远端和本地仓库版本不一致，导致无法推送的情况
	在提交前，使用git pull进行更新一遍
2、使用pycharm时，需要注意，当前是否是在master分支，否则会出现错误
3、进行推送时，需要确定当前版本为最新
```

```
版本回退
git log 【不能查看已经删除的记录】
git reflog 【查看所有分支的所有记录，包括已经删除的记录】
git log --hard HAED^
or
git reflog --hard HEAD~1
or
git reflog --hard 版本号
```

```
撤销：【只能撤销工作区或者时暂存区代码】
# 第一步：将暂存区代码撤销到工作区
git reset HEAD  文件名
# 第二步：撤销工作区代码
git checkout 文件名
```

```
git diff对比版本
```

```
打标签
 git tag -a 标签名 -m '标签描述'
 例：
 git tag -a v1.0 -m 'version 1.0'
推送标签到远程仓库
 git push origin 标签名
 例：
 git push origin v1.0
```

```
分支
master分支：默认分支
dev分支：用于开发的分支，开发结束后需要合并到master分支
git branch --查看当前分支
git checkout -b dev --创建dev分支
设置推送
git push -u origin dev
合并分支
1、先切换到master分支
git checkout master
2、将dev分支合并到master分支
git merge dev
3、推送
git push
```







