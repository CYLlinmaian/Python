'''
Author: CYLlinmaian
Date: 2022-09-04 19:36:43
LastEditTime: 2022-09-04 19:43:28
LastEditors: CYLlinmaian
Description: 输出当前计算机的系统日期和时间
FilePath: \Python-1\例程\日期和时间的输出.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
from datetime import datetime   #引用datetime库
now=datetime.now()  #获得当前日期和时间信息
print(now)
now.strftime("%x")
now.strftime("%X")