'''
Author: CYLlinmaian
Date: 2022-07-25 08:54:02
LastEditTime: 2022-07-25 09:02:15
LastEditors: CYLlinmaian
Description: 
FilePath: \Python\17.嵌套循环.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
'''输出一个三行四列的矩形'''
for i in range(1, 4):  # 行表,执行三次,一次一行
    for j in range(1, 5):
        print('*', end='\t')  # 不换行输出
    print()
