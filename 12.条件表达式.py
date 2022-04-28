#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/28 9:25
# @Author  : CYLlinmaian
# @FileName: 12.条件表达式.py
# @Software: PyCharm
'''
条件表达式   if...else...的简写
    #语法结构:
    x if 判断条件 else y
    #运算规则:
    如果判断条件的布尔值为Ture,条件表达式的返回值为x;判断条件的布尔值为False,条件表达式的返回值为y
'''
#要求从键盘录入两个整数,比较大小
num_a=int(input('请输入第一个整数:'))
num_b=int(input('请输入第二个整数:'))
'''
一般写法
if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)
'''
#使用条件表达式
print('正在使用条件表达式判断...')
'''
①
print((num_a,'大于等于',num_b) if num_a>=num_b else (num_a,'小于',num_b))
'''
#②
print(str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b))
