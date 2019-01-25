# pyUDF


## 1. UDF, UDAF UDTF
- UDF: `User-Defined-Function`
> - UDF函数可以直接应用于select语句，对查询结构做格式化处理后，再输出内容。
- UDAF: `User- Defined Aggregation Funcation`
> - 是对一列整体做计算的聚合函数
- UDTF: `User-Defined Table-Generating Functions`
> - 用来解决 输入一行输出多行(On-to-many maping) 的需求。

## 1. 装饰函数





## 2. An UDF Example
> http://help.aliyun-inc.com/internaldoc/detail/34533.html?spm=a2c1f.8259794.2.11.65fe96d5oCtDot

1. ODPS UDF的Python版本为2.7