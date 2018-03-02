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

#### 3. 把当前文件夹中的所有文件加到git库中, 并commit到本地的master分支
```
git add .
git commit

```

#### 4. 把本地的git库同步commit到remote库
```
git remote add origin git@github.com:ag300g/learnpy.git
git push -u origin master
```