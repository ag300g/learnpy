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

#### 8. 合并本地commit历史来保持树的整洁

`git rebase`是对commit history的改写。
当你要改写的commit history还没有被提交到远程repo的时候，也就是说，还没有与他人共享之前，commit history是你私人所有的, 这时可以使用`git rebase`把自己的小提交合并成一个整的提交, 再把这个整的提交push到远程repo.
> 1. 假如Tom和Jerry共同使用一个远程repo, 并且各自clone到了自己的机器上, 这时Tom和Jerry的机器中有一模一样的两个branch: master和origin/master
> 2. Tom和Jerry各自开发自己新的feature并不断的commit到各自本地的master中，所以他们的master指针不断的向前推移，分别指向不同的commit。而又由于他们都没有git fetch和git push，所以他们的origin/master都维持不变。
> 3. 这时Tom首先把他的commit提交的远程repo中，那么origin/master指针则会前进，和他本机中master指针保持一致
> 4. 现在Jerry也想把他的commit提交到远程repo上去，运行git push，毫无意外的失败了，所以他git fetch了一下，把远程repo，也就是之前Tom提交的T1给拉到了他本机repo中, 这时, 从Jerry的角度看, commit history出现了分叉
> 5. 想要把tom之前提交的内容包含到自己的工作中来, 有两种办法:
> > - `git merge`, 它会自动生成一个commit,既包含Tom的提交也包含Jerry的提交. 这样commit history中的分叉又和到了一起
> > - `git rebase`, 通过`git rebase`后, Jerry的提交被被整合到了Tom提交的后面, 而commit history还是一条直线

想要维持树的整洁, 方法是: 在`git push`之前，先`git fetch`，再`git rebase`。
```bash
git fetch origin master
git rebase origin/master
git push
```
详见: [GitPro_rebase](https://git-scm.com/book/zh/v2/Git-分支-变基)