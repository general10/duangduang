# -*- coding: UTF-8 -*-

import MySQLdb
import time
import comments

def addtable(excelname):
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "rootpwd", "used", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    addtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    sql = comments.inserttmp % (str(addtime), str(excelname))
    print(sql)
    cursor.execute(sql)
    db.commit()