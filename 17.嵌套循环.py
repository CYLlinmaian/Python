'''
Author: CYLlinmaian
Date: 2022-07-25 08:54:02
LastEditTime: 2022-07-25 09:45:20
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


# 三角形
for i in range(1, 10):  # 行数
    for j in range(1, i+1):
        print('*', end='')
    print()

# 九九乘法表
for i in range(1, 10):  # 行数
    for j in range(1, i+1):
        print(i, '*', j, '=', i*j, end='\t')
    print()


# 二重循环中的break和continue用于控制本层循环
'''流程控制语句break和continue在二重循环中的使用'''
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            # break
            continue
        print(j, end='\t')
    print()
