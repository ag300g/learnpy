## 从csv建表

#### 1. 建立一张空表
需要定义表头和类型
```
#!/bin/bash

##  create hive table from a local .csv

sql = "
create table dev.robot123_other_city_map_deliverycenter
(
  province_id varchar(500),
  city_id varchar(500),
  delv_center_num  varchar(500)
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
"
hive "$sql"

```

#### 2. 把csv表的表头去掉
直接在原文件上修改
```
sed -i 1d test.txt
```
命名成新的文件名
```
sed 1d test.txt > test_new.txt
```

#### 3. 把csv文件数据插入到建好的表中
```$xslt
hive "load data local inpath '/home/other_city_map_deliverycenter.csv' into table dev
.robot123_other_city_map_deliverycenter;"
```
> `into`是追加
> `overwrite into`是覆盖