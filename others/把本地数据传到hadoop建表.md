## 从csv建表1
```
drop table if exists dev.robot123_train_sku_basic_info;
create table dev.robot123_train_sku_basic_info
(
sku_name string,
item_name string,
item_desc string,
data_type int,
brand_codes string,
barndname_en string,
barndname_cn string,
barndname_full string,
item_origin string,
qgp int,
sku_valid_flag int,
item_valid_flag int,
sku_status_cd int,
item_status_cd string,
item_first_cate_cd int,
item_first_cate_name string,
item_second_cate_cd int,
item_second_cate_name string,
item_third_cate_cd int,
item_third_cate_name string,
shelves_tm string,
shelves_dt string,
otc_tm string,
utc_tm string,
support_cash_on_deliver_flag string,
vender_direct_delv_flag string,
slogan string,
sale_qtty_lim string,
first_into_wh_tm string,
item_type string,
size string,
size_rem string,
size_seq string,
len string,
width string,
height string,
calc_volume string,
wt string,
colour string,
pac_propt string,
pac_spec string,
free_goods_flag string,
item_sku_id_hashed string,
main_sku_id_hashed string
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' TBLPROPERTIES ("skip.header.line.count"="1");
LOAD DATA LOCAL INPATH 'train_sku_basic_info.csv' OVERWRITE INTO TABLE dev.robot123_train_sku_basic_info;
alter table dev.robot123_train_sku_basic_info set serdeproperties ('serialization.encoding'='GBK');
```

## 从csv建表2

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

#### 4. 遇到有中文的表, 需要改变编码

```$xslt
ALTER TABLE dev.robot123_other_promotion_record SET SERDEPROPERTIES ('serialization.encoding'='GBK');
```
