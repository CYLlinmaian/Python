#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/28 20:59
# @Author  : CYLlinmaian
# @FileName: 15.程序的循环结构.py
# @Software: PyCharm
'''
循环结构
    #反复做同一件事情的情况,称为循环
    #循环结构的分类
        ①while
        ②for -in
    #语法结构
        while 条件表达式
            条件执行体(循环体)
    #选择结构的if与循环结构的while的区别
        ①if是判断一次,条件为Ture执行一次
        ②while是判断N+1次,条件为True执行N次
while循环的执行流程
    #四步循环法
        ①初始化变量
        ②条件判断
        ③条件执行体(循环体)
        ④改变变量
        总结:初始化变量与条件判断的变量与改变的变量为同一个变量
'''
#实例
'''
#选择结构if
a=1
if a<10:
    print(a)
    a+=1
    
#循环结构while
a=1
while a<10:
    print(a)
    a+=1
'''
sum=0
a=0
while a<101:
    sum+=a
    a+=1
print('0到100的和为:',sum)
#!!!警告,注意缩进,不要将print写入循环

#练习 计算1到100之间的偶数和
sum=0
a=1
while a<=100:
    if a%2==0:  #'if a%2:'奇数和条件
        sum+=a
    a+=1
print('1~100之间的偶数和为:',sum)