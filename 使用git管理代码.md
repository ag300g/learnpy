#### 1. 切换到想要建库的文件夹, 建立本地git库
```
cd ****/****/
git init
```

#### 2. 设置自己的名字和邮箱
```
git config --global user.name ag300g
git config --global user.email ag300g@163.com
```
只有当名字和remote的用户名一致时, 才会记录commit
> 不加`--global`只在当前git库中使用此名字

#### 3. 把当前文件夹中的所有文件加到git库中, 并commit到本地的master分支
```
git add .
git commit -a -m 'update **'

```

#### 4. 把本地的git库同步commit到remote库
```
git remote add origin git@github.com:ag300g/learnpy.git
git push -u origin master
```
- `-u`是设置了一个默认的远程数据库，在使用来了`-u`之后， 也可以直接使用`git push`
- `-f`在本地与远程不一致且以本地为准的情况下可以直接使用`-f`强行使用本地数据覆盖远端数据

#### 5. 删除 untracked files
```
# 删除 untracked files
git clean -f

# 连 untracked 的目录也一起删掉
git clean -fd

# 连 gitignore 的untrack 文件/目录也一起删掉 （慎用，一般这个是用来删掉编译出来的 .o之类的文件用的）
git clean -xfd

# 在用上述 git clean 前，墙裂建议加上 -n 参数来先看看会删掉哪些文件，防止重要文件被误删
git clean -nxfd
git clean -nf
git clean -nfd
```

#### 6. 把远程更新同步到本地
```
git pull origin master
```
上述命令其实相当于`git fetch` 和 `git merge`
在实际使用中，`git fetch`更安全一些，因为在`merge`前，我们可以查看更新情况，然后再决定是否合并。

#### 7. 使新设置的.gitignore生效
需要先删除缓存，然后把所有文件重新添加一次，然后先把.gitignore提交了，然后再把所有文件同步到远程库
```
git rm -r --cached .  #清除缓存
git add . #重新trace file
git commit -m "update .gitignore" #提交和注释
git push origin master #可选，如果需要同步到remote上的话
```



