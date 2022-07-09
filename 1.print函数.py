'''
Author: CYLlinmaian
Date: 2022-07-10 03:38:22
LastEditTime: 2022-07-10 03:38:43
LastEditors: CYLlinmaian
Description: 
FilePath: \Python\1.print函数.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
# 输出数字

print(23.5)

# 输出字符串，但字符串需要用引号，不用引号会报错

print('helloword')
print('赛悠啦啦')

# 输出含有运算符的表达式

print(3 - 1)
print(5 + 1)

# 将数据输出到文件中
# ！！！需要注意：1、所指定的盘符存在；2、使用file=fp
fp = open('C:/Users/CYLlinmaian/Desktop/X.txt', 'a+')  # "a+"如果文件不存wariness在就创建，存在就在文件内容的后面继续追加
print('helloword', file=fp)
fp.close()

# 不进行换行输出

print('hello', 'word', 'see you lala')
