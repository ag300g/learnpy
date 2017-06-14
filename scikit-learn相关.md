### `CountVectorizer`
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