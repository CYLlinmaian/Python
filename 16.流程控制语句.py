'''
Author: CYLlinmaian
Date: 2022-07-10 18:50:07
LastEditTime: 2022-07-10 21:26:44
LastEditors: CYLlinmaian
Description: 
FilePath: \Python\16.流程控制语句.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''

# break语句
# 用于结束循环，通常与分支结构if一起使用
'''从键盘录入密码，最多输三次，密码正确结束循环'''

for item in range(3):
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
