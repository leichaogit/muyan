# 数据库和sql

1、创建表的create table 语句：

1. 列名、数据类型、该列所需的约束
2. 该表所需的约束（主键,用来唯一确定一行数据[不能有重复]）

```sql
create table product
(
    product_id char(4) not null,
    product_name varchar(100) not null,
    product_type varchar(32) not null,
    sale_price integer,
    purchase_price integer,
    regist_date date,
    primary key(product_id)
);
```

2、定义表的更新alter table语句(alter:改变)：

1. 增加一列
   1. alter table 表名 add (列名 + 约束)；
2. 删除一列
   1. alter table 表名 drop(列名)；
3. 重命名
   1. rename table 旧表名 to 新表名;(在MySQL中的写法，其他的有所区别)
   2. alter table 表名 change 旧列名 新列名 约束;
4. 修改字段
   1. alter table 表明 modify 列名 约束;

   注意，对表的定义进行更新后，无法进行恢复，只能重新进行输入。

3、向product表中插入数据：

```sql
--插入数据
start transaction;
insert into product values
("0001","T恤衫","衣服",1000,500,"2019-09-20"),
("0002","打孔器","办公用品",500,320,"2019-9-11"),
("0003","运动T恤","衣服",4000,2800,"2019-09-20"),
("0004","菜刀","厨房用具",3000,2800,"2019-01-15"),
("0005","高压锅","厨房用具",6800,5000,"2019-01-20"),
("0006","叉子","厨房用具",500,null,"2019-01-23"),
("0007","擦菜板","厨房用具",880,790,"2019-02-22"),
("0008","圆珠笔","办公用品",100,null,"2019-02-12");
commit;
```

4、数据类型的指定

1. integer型：存整数，不能存小数
2. int型：整数
3. char型：存定长字符串，不足的补空格
4. varchar型：存不定长的字符串
5. date型：用来存日期

课后练习：

```sql
create database my_sql_test charset="utf8";
create table addressbook(
	regist_no integer not null,
    name varchar(128) not null,
    address varchar(256) not null,
    tel_no char(10) null,
    mail_address char(20) null
);
alter table addressbook add postal_code char(8) not null;
```

