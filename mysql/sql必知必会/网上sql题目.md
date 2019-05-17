```sql
一,基本表的定义与删除.

题1: 
用SQL语句创建如下三张表：学生（Student）,课程表（Course）,和学生选课表（SC）,这三张表的结构如表1-1到表1-3所示。
表1-1 Student表结构
列名	说明	数据类型	约束
Sno	学号	字符串，长度为7	主码
Sname	姓名	字符串，长度为10	非空
Ssex	性别	字符串，长度为2	取‘男’或‘女’
Sage	年龄	整数	取值15~45
Sdept	所在系	字符串，长度为20	默认为‘计算机系’


create table Student(
Sno char(7) primarykey,
Sname char(10) not null,
Ssex char(4) check(Ssex='男' or Ssex='女') ,
Sage number() check(Sage>=15 and Sage<=45),
Sdept char(20) default('计算机系'));
-------------------------------------------------------------------------------------------------------------------


表1-2Course表结构
列名	说明	数据类型	约束
Cno	课程号	字符串，长度为10	主码
Cname	课程名	字符串，长度为20	非空
Ccredit	学分	整数	取值大于0
Semster	学期	整数	取值大于0
Period	学时	整数	取值大于0


create table Course(
Cno char(10) primarykey,
Cname char(20) not null,
Ccredit nuber() check(Ccredit>0) ,
Cemster number() check(Cemster>0),
Period number() check(Period>0));
-----------------------------------------------------------------------------------------------------------------

表1-3 SC表结构
列名	说明	数据类型	约束
Sno	学号	字符串，长度为7	主码，引用Student的外码
Cno	课程名	字符串，长度为10	主码，引用Course
Grade	成绩	整数	取值0~100

 

create table SC(
Sno char(7), 
Cno char(10),

primary key(Sno,Cno),

foreign key (Sno) references Student(Sno),
foreign key (Cno) references.3 Course(Cno),

Grade number() check(Grade>=0 and Grade<=100));

-------------------------------------------------------------------------------------------------------------------

二，修改表结构

题2：
为SC表添加“选课类别”列，此列的定义为XKLB char(4).
alter SC set add XLB char(4) null;

题3：
将新添加的XKLB的类型改为char(6)。
alter table SC alter column XKLB char(6);

题4：
删除Course表的Period列。
alter from drop column Period;

三，数据查询功能

表3-1 Student表数据
Sno	Sname	Ssex	Sage	Sdept
9512101	李勇	男	19	计算机系
9512102	刘晨	男	20	计算机系
9512103	王敏	女	20	计算机系
9521101	张立	男	22	信息系
9521102	吴宾	女	21	信息系
9521103	张海	男	20	信息系
9531101	钱小平	女	18	数学系
9531102	王大力	男	19	数学系

 

insert into Student(Sno,Sname,Ssex,Sage,Sdept)
values(
'9512101','李勇','男',19,'计算机系';
'9512102','刘晨','男',20,'计算机系';
'9512103','王敏','女',20,'计算机系';
'9521101','张立','男',22,'信息系';
'9521102','吴宾','女','21','信息系';
'9521103','张海','男',20,'信息系';
'9531101','钱小平','女',18,'数学系';
'9531102','王大力','男',19,'数学系')
-------------------------------------------------------------------------------------------------------------------

表3-2 Course表数据
Cno	Cname	Ccredit	Cemester
C01	计算机文化学	3	1
C02	VB	2	3
C03	计算机网络	4	7
C04	数据库基础	6	6
C05	高等数学	8	2
C06	数据结构	5	4


insert into Course(Cno,Cname,Ccredit,Cemester) values(
'C01','计算机文化学',3,1;
'C02','VB',2,3;
'C03','计算机网络',4,7;
'数据库基础',6,6;
'C05','高等数学',8,2;
'C06','数据结构',5,4)
-------------------------------------------------------------------------------------------------------------------

表 3-3 SC表数据
Sno	Cno	Grade	XKLB
9512101	c01	90	必修
9512101	c02	86	选修
9512101	c06	<NULL>	必修
9512102	c02	78	选修
9512102	c04	66	必修
9521102	c01	82	选修
9521102	c02	75	选修
9521102	c04	92	必修
9521102	c05	50	必修
9521103	c02	68	选修
9521103	c06	<NULL>	必修
9531101	c01	80	选修
9531101	c05	95	必修
9531102	c05	85	必修


insert into SC values(
'9512101','c01',90,'必修';
'9512101','c02',86,'选修';
'9512101','c06',NULL,'必修';
'9512102','c02',78,'选修';
'9512102','c04',66,'必修';
'9521102','c01',82,'选修';
'9521102','c02',75,'选修';
'9521102','c04',92,'必修';
'9521102','c05',50,'必修';
'9521103','c02',68,'选修';
'9521103','c06',NULL,'必修';
'9531101','c01',80,'选修';
'9531101','c05',95,'必修';
'9531102','c05',85,'必修')

insert into SC(Sno,Cno,Grade) values('9521102','C02',75,'选修')
insert into SC values('9521102','C04',92,'必修')
insert into SC values('9521102','C05',50,'必修')
insert into SC values('9521103','C02',68,'选修')
insert into SC values('9521103','C06',NULL,'必修')
insert into SC values('9531101','C01',80,'选修')
insert into SC values('9531101','C05',95,'必修')
insert into SC values('9531102','C05',85,'必修')

 

-------------------------------------------------------------------------------------------------------------------

题5：
用sql语句填写以上（表3-1 Student表数据、表3-2 Course表数据、表 3-3 SC表数据）数据。


题6：
查询全体学生的学号与姓名。
select Sno,Sname from Student;

题7：
查询全体学生的姓名，学号和所在系。
select Sno,Sname,Sdept from Student;

题8：
查询全体学生的记录。

select * from SC join Student on Student.Sno=SC.Sno;


题9：
查询全体学生的姓名及其出生年份。
select Sname,2011-Sage as '出生年份';

题10：
查询全体学生的姓名和出生年份，并在出生年份列前加入一个列，此列的每行数据均为“Year of Birth”常量值。
select Sname,'出生年份',2011-Sage from Student;

题11：
在选课表（SC）中查询有哪些学生选修了课程，并列出学生的学号。
select distingct Sno from SC;

题12：
查询计算机系全体学生的姓名。
select Sname from Student where Sdept='计算机系';

题13：
查询所有年龄在20岁以下的学生的姓名及年龄。
slect Sname,Sage from Student where Sage<20;

题14：
查询考试成绩不及格的学生的学号。
select distingct Sno from SC where Grade <60;

题15：
查询年龄在20~23岁之间的学生的姓名，所在系和年龄。
select Sname,Sdept,Sage from Student where Sage between 20 and 23;

题16：
查询年龄不在20~23之间的学生的姓名，所在系和年龄。
select Sname,Sdept,Sage from Student where Sage not between 20 and 23;

题17：
查询信息系，数学系和计算机系学生的姓名和性别。
select Sname,Ssex from Student where Sdept in ('信息系','数学系','计算机系');

题18：
查询既不属于信息系，数学系，也不属于计算机系的学生的姓名和性别。
select Sname,Ssex from Student where Sdept not in ('信息系','数学系','计算机系');

题19：
查询姓“张”的学生的详细信息。
select * from Student where Sname like '张%';

题20：
查询学生表中姓“张”，姓“李”和姓“刘”的学生的情况。
select * from Student where Sname like '[张李刘]%';

题21：
查询名字中第2个字为“小”或“大”字的学生的姓名和学号。
select Sname,Sno from Student where Snme like '_[小大]%';

题22：
查询所有不姓“刘”的学生。
select Sname from Student where Sname not like '刘%';

题23：
从学生表中查询学号的最后一位不是2，3，5的学生的情况。
select * from where Sno not like '%[235]';

题24：
查询无考试成绩的学生的学号和相应的课程号。
select Sno,Cno from SC where Grade is null;

题25：
查询所有有考试成绩的学生的学号和课程号。
select Sno,Cno from SC where Grade is not null;

题26：
查询计算机系年龄在20岁以下的学生的姓名。
select Sname from Student where Sdept = '计算机系' and Sage < 20;

题27：
将学生按年龄升序排序。
select * from Student order by Sage;

题28：
查询选修了课程“c02”的学生的学号及其成绩，查询结果按成绩降序排列。
select Sno,Grade from SC where Cno='c02' order by Grade desc;

题29：
查询全体学生的信息，查询结果按所在系的系名升序排列，同一系的学生按年龄降序排列。
select * from Student order by Sdept,Sage desc;

题30：
统计学生总人数。
select count(*) from Student;

题31：
统计选修了课程的学生的人数。
select count(distingct Sno) from SC;

题32 ：
计算学号为9512101的学生的考试总成绩之和。
select sum(Grade) from SC where Sno='9512101';

题33：
计算课程“c01”的学生的考试平均成绩。
select avg(Grade) from SC where Cno='c01';

题34：
查询选修了课程“c01”的学生的最高分和最低分。
select max(Grade),min(Grade) from SC where Cno='c01';

题35：
统计每门课程的选课人数，列出课程号和人数。
select Cno as '课程号',count(Sno) as '选课人数' from SC group by Cno;

题36：
查询每名学生的选课们数和平均成绩。
select Sno as '学号',count(*) as '选课门数',avg(Grade) as '平均成绩' from SC group by SNo;

题37：
查询选修了3门以上课程的学生的学号。
select Sno from SC group by Sno having count(*) > 3;

题38：
查询选课门数等于或大于4门的学生的平均成绩和选课门数。
select Sno,avg(Grade) '平均成绩',count(*) '选课门数' from SC group by Sno having count(*) >= 4;

四,多表连接查询。

题39：
查询每个学生的情况及其选课的情况。
select * from Student join SC on Student.Sno=SC.Sno

题40：
去掉例38中的重复列。
select Sno,avg(Grade) '平均成绩',count(distingct Sno) '选课门数' from SC group by Sno having count(*) >= 4;


题41：
查询计算机系学生的选课情况，要求列出学生的名字，所修课的课程号和成绩。
select Sname,Cno,Grade from Student join SC on Student.Sno=SC.Sno where Sdept = '计算机系';

题42：
查询信息系选修VB课程的学生的成绩，要求列出学生姓名，课程名和成绩。
select Sname,Cname,Grade from Student s join SC on s.Sno=SC.Sno join Course c on c.Cno=SC.Cno 
where Sdept = '信息系' and Cname = 'VB';

题43：
查询所有选修了VB课程的学生的情况，要求列出学生姓名和所在的系。
select Sname,Cname,Grade from Student s join SC on s.Sno=SC.Sno join Course c on c.Cno=SC.Cno 
where Cname = 'VB';

题44：
查询与刘晨在同一个系学习的学生的姓名和所在系。
select S2.Sname,S2.Sdept from Student S1 join Student S2 on S1.Sdept = S2.Sdept 
where S1.Sname = '刘晨' and S2.Sname !='刘晨';

题45：
查询学生的选课情况，包括选修课程的学生和没有修课的学生。
select Student.Sno,Sname,Cno,Grade from Student left outer join SC on Student.Sno = SC.Sno;

五，自查询。

题46：
查询与刘晨在同一个系的学生。
select Sno,Sname,Sdept from Student where Sdept in (
select Sdept from Student
where Sname='刘晨') and Sname='刘晨';

题47：
查询成绩大于90分的学生的学号和姓名。
select Sno,Sname from Student 
where Sno in (select Sno from SC where Grade > 90);

题48：
查询选修了“数据库基础”课程的学生的学号和姓名。
select Sno,Sname from Student where Sno in
(
select Sno from SC where Cno in
(
select Cno from Course
where Cname='数据库基础'
)
);

题49：
查询选修了课程“c02”且成绩高于次课程的平均成绩的学生的学号和成绩。
select Sno,Grade from SC where Cno='c02' and
Grade >(select avg(Grade) from SC where Cno = 'c02');

题50：
查询选修了课程“c01”的学生姓名。
select Sname from Student 
where exists ( select * from SC where Sno = Student.Sno and Cno='c01');

题51：
查询没有选修课程“c01”的学生姓名和所在系。
select Sname,Sdept from Student 
where not exists ( select * from SC where Sno = Student.Sno and Cno='c01');

六，自查询。

题52：
查询选修了课程“c01”的学生的姓名和所在系。
select Sname,Sdept from Student 
where exists ( select * from SC where Sno = Student.Sno and Cno='c01');

题53：
查询数学系成绩在80分以上的学生的学号，姓名。
select Sname,Sno from Student 
where exists ( select * from SC where Sno = Student.Sno and Grade>=80);

题54：
查询计算机系考试成绩最高的学生的姓名。
select Sname from Student 
where exists ( select * from SC where Sno = Student.Sno and max(Grade));

七，插入数据
题55：
将新生纪录（9521105，陈冬，男，信息系，18岁）插入到Student表中。
insert into Student values('9521105','陈冬','男',18,'信息系');

题56：
在SC表中插入一新记录（9521105，c01），成绩暂缺。
insert into SC values('9521105','c01',null,'必修');

八，更新数据。

题57：
将所有学生的年龄加1。
update Student set Sage = Sage+1;

题58：
将“9512101”学生的年龄改为21岁。
update Student Sage=21 where Sno='9512101';

题59：
将计算机系学生的成绩加5分。
update SC set Grade = Grade + 5 where Sno in (select Sno from Student where Sdept='计算机系');

九，删除数据。

题60:
删除所有学生的选课记录。
delete from SC;

题61：
删除所有不及格学生的选课记录。
delete from SC where Grade < 60;

题62：
删除计算机系不及格学生的选课记录。
delete from SC where Grade < 60 and Sno in (select Sno from Student where Sdept = '计算机系');
```

