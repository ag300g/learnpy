### 字典类及相关方法
1. 创建一个字典
> - `d=dict()`或者`d={}`
> - 往字典中加东西: `d['one']='Michael'`
> - `dic1 = {'a': [1, 1, 1, 2, 2, 2], 'b': [2, 3, 4, 2, 3, 4], 'c': ['s', 's', 's', 's', 's', 's'], 'd': [6, 5, 4, 3, 2, 1]}`
2. 字典是**无序**的, 是一个hash table
3. `len(d)` 键值对的长度
4. `'one' in d` 'one'是否在字段的**键**中
5. `get()`
> - 字典的一个方法, `d.get('one','not found')`
> - 如果'one'在字典的**键**中, 则返回对应的**值**, 否则返回'not found'
6. 快速创建字典
> `d=dict(zip('abcdefg',range(7)))`
7. `update()`
> 接收一个元组列表, 并将它们作为键值对添加到一个已有的字典中

8. 访问字典中某个键值对
> `dic1.items()[0]`

9. 遍历字典中的键值对
```python
dic1 = {'a': [1, 1, 1, 2, 2, 2], 'b': [2, 3, 4, 2, 3, 4], 'c': ['s', 's', 's', 's', 's', 's'], 'd': [6, 5, 4, 3, 2, 1]}
for a, b in dic1.items():
    print a,
    print b
```