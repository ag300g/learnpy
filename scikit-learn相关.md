## `CountVectorizer`
```python
## 从文本中抽取特征
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorize()
vectorizer.fit_transform(a) # a是pandas.core.series.Series类型

vectorizer.transform(b) # b是pandas.core.series.Series类型

```
[详见sklearn网站说明](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)
1. CountVectorize()参数`min_df`
> - default=1

> - 如果没有参考词典, 则会根据实际的内容建立词典, 这时min_df若设置成**整数**, 则在实际文章中出现的**次数**<min_df的词不会建到字典中来

> - 如果没有参考词典, 则会根据实际的内容建立词典, 这时min_df若设置成[0,1]之间的**小数**, 则在实际文章中出现的**频率**<min_df的词不会建到字典中来

2. CountVectorize()参数`max_df`:
> - default=1.0

> - 如果没有参考词典, 则会根据实际的内容建立词典, 这时max_df若设置成[0,1]之间的**整数**, 则在实际文章中出现的**次数**>max_df的词不会建到字典中来

> - 如果没有参考词典, 则会根据实际的内容建立词典, 这时max_df若设置成[0,1]之间的**小数**, 则在实际文章中出现的**频率**>max_df的词不会建到字典中来

3. CountVectorize()参数`vocabulary`: 向量化时的参考词典, 可以实现通过dic的方式输入, 也可以实现不输入

4. 方法`fit_transform`

5. 方法`transform`


## `Preprocessing`
1. `scaler()` 特征向量标准化
[详见sklearn网站说明](http://scikit-learn.org/stable/modules/preprocessing.html)
```python
from sklearn import preprocessing
import numpy as np
X = np.array([[ 1., -1.,  2.],[ 8.,  0.,  0.], [ 0.,  1., -1.]])
X_scaled = preprocessing.scale(X)
# X_scaled的每列特征都转换成其z-score
# 缺点, 无法对新变量使用同样的方法

scaler = preprocessing.StandardScaler().fit(X) # 在没有设置任何参数的情况下, 可以把X进行按照每列的分布归一化到N(0,1)
print(scaler.mean_)
print(scaler.scale_)
print(scaler.transform(X))


scaler.transform([[-1., -1., -1.]])   # 把一个新的行向量(list of list)分别按照之前的列分布进行标准化

min_max_scaler = preprocessing.MinMaxScaler()  ## (x-min)/(max-min)
X_minmax = min_max_scaler.fit_transform(X)

print(X_minmax)

min_max_scaler.transform([[100,100,100]])
```

2. `LabelEncoder()` 为分类问题中的类别设置标签

```python
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(["paris", "paris", "tokyo", "amsterdam"])

list(le.classes_)
le.transform(["tokyo", "tokyo", "paris"]) # 把一个新向量(list)按照之前的规则编码
list(le.inverse_transform([2, 2, 1])) # 把一个编码按照之前的规则转化成值
```

## `KFold`

```python
from sklearn.cross_validation import KFold
X = np.array([[1, 2], [3, 4], [1, 2], [3, 4], [1, 2], [3, 4]])
y = np.array([1, 2, 3, 4, 5, 6])
kf = KFold(6, n_folds=3, shuffle=True)


for train_index, test_index in kf:
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
```
> 通过`train_index`和`test_index`可以把训练集按照一定的折数进行分组

> 参数`shuffle=TRUE`可以先把行的顺序随机打乱然后再进行分组

> [详见sklearn网站说明](http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.KFold.html)