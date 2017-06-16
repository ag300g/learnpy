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

> - 如果没有参考词典, 则会根据实际的内容建立词典, 这时min_df若设置成[0,1]之间的**整数**, 则在实际文章中出现的**次数**<min_df的词不会建到字典中来

> - 如果没有参考词典, 则会根据实际的内容建立词典, 这时min_df若设置成[0,1]之间的**小数**, 则在实际文章中出现的**频率**<min_df的词不会建到字典中来

2. CountVectorize()参数`max_df`:
> - default=1.0

> - 如果没有参考词典, 则会根据实际的内容建立词典, 这时max_df若设置成[0,1]之间的**整数**, 则在实际文章中出现的**次数**>max_df的词不会建到字典中来

> - 如果没有参考词典, 则会根据实际的内容建立词典, 这时max_df若设置成[0,1]之间的**小数**, 则在实际文章中出现的**频率**>max_df的词不会建到字典中来

3. CountVectorize()参数`vocabulary`: 向量化时的参考词典, 可以实现通过dic的方式输入, 也可以实现不输入

4. 方法`fit_transform`

5. 方法`transform`


## `Preprocessing`
特征向量标准化
[详见sklearn网站说明](http://scikit-learn.org/stable/modules/preprocessing.html)
```python
from sklearn import preprocessing
import numpy as np
X = np.array([[ 1., -1.,  2.],[ 8.,  0.,  0.], [ 0.,  1., -1.]])
X_scaled = preprocessing.scale(X)
# X_scaled的每列特征都转换成其z-score

scaler = preprocessing.StandardScaler().fit(X)
# 在没有设置任何参数的情况下, 可以把X进行按照每列的分布归一化到N(0,1)
print(scaler.mean_)
print(scaler.scale_)
print(scaler.transform(X))

scaler.transform([[-1.,  1., 0.]])    ## 把一个新的列向量按照之前的标准归一化


min_max_scaler = preprocessing.MinMaxScaler()  ## (x-min)/(max-min)
X_train_minmax = min_max_scaler.fit_transform(X_train)

X_train_minmax

```

