'''
Author: CYLlinmaian
Date: 2022-09-04 21:58:17
LastEditTime: 2022-09-04 22:15:44
LastEditors: CYLlinmaian
Description: 华氏温度和摄氏温度的转换
FilePath: \Python-1\例程\温度转换.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
TempStr=input("请输入带有符号的温度值：")
if TempStr[-1] in ['F','f']:
    C=(eval(TempStr[0:-1])-32)/1.8
    print("转换后的温度是{:.2f)C".format(C))
elif TemStr[-1] in ['C','c']:
    F=