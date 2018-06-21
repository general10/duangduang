# -*- coding: utf-8 -*-
import os
import MySQLdb

# create table booklog(
#     time varchar(50),
#     excelname varchar(50)
# );

db = MySQLdb.connect("localhost","root","rootpwd","used")
# db = MySQLdb.connect("10.10.10.5","root","123456")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("use used")
cursor.execute("insert into booklog values (1,2)")
# 使用 fetchone() 方法获取一条数据。
# data = cursor.fetchone()
# 使用 fetchall() 方法获取全部数据。
data = cursor.fetchall()
print data
db.commit()
db.close()