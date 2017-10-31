#!D:/Program Files/Python3.6.0/python 
# -*- coding: utf-8 -*-

'''
  学习MySQL
'''

import  pymysql
conn = pymysql.connect(user='root',password='password',database='worker_info')
cursor = conn.cursor()
# cursor.execute('show tables;')
# if 'worker' in cursor.fetchall():
cursor.execute('drop table worker')
cursor.execute('create table worker (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into worker(id,name)values(%s,%s)',('1','lipeipei'))
cursor.execute('insert into worker(id,name)values(%s,%s)',('2','lipeipei'))
print(cursor.rowcount)
conn.commit()
cursor.close()
#进行查询
cursor = conn.cursor()
cursor.execute('select * from worker where name = %s','lipeipei
print(cursor.rowcount)')
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()


