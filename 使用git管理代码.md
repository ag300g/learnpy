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

#### 6. 把远程更新同步到本地
```
git pull origin master
```
上述命令其实相当于`git fetch` 和 `git merge`
在实际使用中，`git fetch`更安全一些，因为在`merge`前，我们可以查看更新情况，然后再决定是否合并。


