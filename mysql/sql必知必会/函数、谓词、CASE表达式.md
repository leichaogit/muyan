1、各种各样的函数(了解，会用就好)

1. 算术函数

   1. +-*/

   2. numeric(全体位数，小数位数)函数

      ```sql
      --创建samplemath表
      create table samplemath (m numeric(10,3),n integer,p integer);
      ```

      1. abs绝对值函数
      2. mod求余函数
      3. round(对象数值，保留小数位数)四舍五入函数

   2.字符串函数

```sql
create table samplestr (str1 varchar(40),str2 varchar(40),str3 varchar(40));
```

1. concat函数完成拼接

   1. concat(str1,str2,str3)

   2.length函数，求字符串长度

   1. length(字符串)

      注意：对一个字符使用length函数，可能会得到2个字节以上的结果(编码原因)

   3.大小写转换函数

   1. lower(字符串)转化为小写
   2. upper(字符串)转化为大写

   4.replace(字符串)将字符串的一部分替换为其他的字符串

```sql
--用法
replace(对象字符串，需要替换的字符，替换成的字符)
--replace("我在这里","我","你") ==> "你在这里"
```

​	5.substring字符串的截取

```sql
substring(对象字符串 from 截取的起始位置 for 截取的字符数)
```

3.日期函数

1. current_date函数,获取当前日期

   ```sql
   select current_date;
   ```

   2.current_time函数，获取当前时间

   ```sql
   select current_time;
   ```

4.转换函数

1. cast类型转换(方便DBMS内部处理而开发的功能)

   ```sql
   cast(转换前的值 as 想要转换的数据类型)
   select cast('0001' as signed integer) as '整型';
   ```

   2.coalesce将null转换为其他值

   ```sql
   --该函数，会返回可变参数中左侧开始，第一个不是Null的值
   coalesce(数据1，数据2，数据3......)
   select coalesce(null,1) as '测试1',coalesce(null,'test',null) as '测试2',coalesce(null,null,'2019-4-21') as '测试3' ;
   ```

2、谓词

1. 返回值为真值的函数(真值:true、false、unknown)

   1. like 查询

   ```sql
   create table samplelike(strool varchar(6) not null,primary key(strool));
   insert into samplelike values ('abcddd');
   insert into samplelike values ('dddabc');
   insert into samplelike values ('abdddc');
   insert into samplelike values ('abcdd');
   insert into samplelike values ('ddabc');
   insert into samplelike values ('abddc');
   --(%为匹配0个或者任意字符串)
   --(_为匹配1个或者任意字符串)
   --前方一致
   select * from samplelike where strool like 'ddd%';
   --中间一致
   select * from samplelike where strool like '%ddd%';
   --后面一致
   select * from samplelike where strool like '%ddd';
   ```

   2.between范围查询

   ```sql
   --选择在100到1000范围之间的商品，注意会包括100和1000
   select product_name,sale_price from product where sale_price between 100 and 1000;
   --不包括100和1000
   select product_name,sale_price from product where sale_price > 100 and sale_price < 1000;
   ```

   3.is null 和is not null

   4.or 的简便用法

   ```sql
   select product_name,purchase_price from product where purchase_price = 320 or purchase_price = 500 or purchase_price = 5000;
   
   ```

   5.in的特殊用法(可以使用子查询作为其参数)

   ```sql
   --in的用法
   select product_name,purchase_price from product where purchase_price in(320,500,5000);
   --反之，使用not in
   --注意in 和 not in都不能取出null数据
   
   CREATE TABLE ShopProduct
   (shop_id CHAR(4) NOT NULL,
   shop_name VARCHAR(200) NOT NULL,
   product_id CHAR(4) NOT NULL,
   quantity INTEGER NOT NULL,
   PRIMARY KEY (shop_id, product_id));
   --开启事务
   select product_id from ShopProduct where shop_id = '000C';
   BEGIN TRANSACTION; 
   INSERT INTO ShopProduct (shop_id, shop_name, product_id, quantity) VALUES ('000A', '东京', '0001', 30);
   INSERT INTO ShopProduct (shop_id, shop_name, product_id, quantity) VALUES ('000A', '东京', '0002', 50);
   INSERT INTO ShopProduct (shop_id, shop_name, product_id, quantity) VALUES ('000A', '东京', '0003', 15);
   INSERT INTO ShopProduct (shop_id, shop_name, product_id, quantity) VALUES ('000B', '名古屋', '0002', 30);
   INSERT INTO ShopProduct (shop_id, shop_name, product_id, quantity) VALUES ('000B', '名古屋', '0003', 120);
   INSERT INTO ShopProduct (shop_id, shop_name, product_id, quantity) VALUES ('000B', '名古屋', '0004', 20);
   INSERT INTO ShopProduct (shop_id, shop_name, product_id, quantity) VALUES ('000B', '名古屋', '0006', 10);
   INSERT INTO ShopProduct (shop_id, shop_name, product_id, quantity) VALUES ('000B', '名古屋', '0007', 40);
   INSERT INTO ShopProduct (shop_id, shop_name, product_id, quantity) VALUES ('000C', '大阪', '0003', 20);
   INSERT INTO ShopProduct (shop_id, shop_name, product_id, quantity) VALUES ('000C', '大阪', '0004', 50);
   INSERT INTO ShopProduct (shop_id, shop_name, product_id, quantity) VALUES ('000C', '大阪', '0006', 90);
   INSERT INTO ShopProduct (shop_id, shop_name, product_id, quantity) VALUES ('000C', '大阪', '0007', 70);
   INSERT INTO ShopProduct (shop_id, shop_name, product_id, quantity) VALUES ('000D', '福冈', '0001', 100);
   --关闭事务
   COMMIT;
   select product_id from ShopProduct where shop_id = '000C'
   select product_name,sale_price from product where product_id in (select product_id from ShopProduct where shop_id = '000C') ;
   ```

   注意：使用子查询可以使得程序易于维护

   5.exist：理解较为复杂

   ```sql
   --此处的select * 为一种书写习惯
   SELECT product_name, sale_price FROM Product AS P WHERE EXISTS (SELECT * FROM ShopProduct AS SP WHERE SP.shop_id = '000C' AND SP.product_id = P.product_id);
   ```

3、CASE表达式(条件分支)

1. 搜索case表达式

   ```sql
   case when <求值表达式> then <表达式> 
      	 when <求值表达式> then <表达式> 
   	 when <求值表达式> then <表达式>
        else <表达式>
   end
   --when 中为真就执行then，否则执行else
   ```

   ```sql
   select product_name ,
   case when product_type = '衣服' then concat('A:',product_type)
        when product_type = '办公用品' then concat('B:',product_type)
        when product_type = '厨房用具' then concat('C:',product_type)
   else null
   end as abc_product_type
   from product;
   ```

   ```sql
   --练习题
   --6-1
   --显示进价不在500，2800，5000中的商品信息和进价
   --错误，not in中不能使用null
   --6-2
   select sum(case when sale_price <= 1000 then 1 else 0 end) as low_price,
   	   sum(case when sale_price between 1001 and 3000 then 1 else 0 end) as mid_price,
   	   sum(case when sale_price >= 3001 then 1 else 0 end) as high_price
   	from product;
   ```

   