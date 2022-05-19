#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/28 10:18
# @Author  : CYLlinmaian
# @FileName: 13.pass语句.py
# @Software: PyCharm
'''
pass语句:
    语句啥都不干,只是一个占位符,用在语法上需要语句的地方
啥时候使用:
    先搭建语法结构,还没想好代码怎么写的时候
哪些语句一起使用
    ①if语句的条件执行体
    ②for-in语句的循环体
    ③定义函数时的函数体
'''
answer = input('您是会员吗?Y/N:')
money = float(input('请输入您的购物金额:'))
if answer == 'Y':
    pass
elif answer == 'N':
    pass
else:
    pass
