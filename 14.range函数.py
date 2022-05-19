#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/28 20:05
# @Author  : CYLlinmaian
# @FileName: 14.range函数.py
# @Software: PyCharm
'''
range()函数
    #用于生成一个整数序列
    #创建range对象的三种方式:
        ①range(stop)---创建一个[0,stop)之间的整数序列,步长为1
        ②range(start,stop)---创建一个[start,stop)之间的整数序列,步长为1
        ③range(start,stop,step)------创建一个[start,stop)之间的整数序列,步长为step
    #返回值是一个迭代器对象
    #range类型的优点
        range只需要存储start,stop,step三个值,不管整数序列有多长,range对象占用的内存空间相同,只有用到range对象时,才会去计算序列中的相关元素
        in与not in 判断整数序列中是否存在(不存在)指定的整数
'''
# 创建range对象的三种方式
'''第一种创建方式,只有一个参数,未指定起始值'''
r = range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],默认从0开始,默认相差1,称为步长
print(r)
print(list(r))  # 查看range对象中的整数序列    -->list是列表的意思

'''第二种创建方式,给了两个参数,指定了起始值'''
r = range(1, 10)  # 指定了起始值,从1开始,到10结束(不包含10),默认步长为1
print(r)
print(list(r))

'''第三种创建方式,给了三个参数,指定了起始值和步长'''
r = range(1, 10, 2)  # 指定了起始值和步长,从1开始,到10结束(不包含10),步长为2
print(r)
print(list(r))

'''判断指定的整数在序列中是否存在  in,not in'''
print(10 in r)
print(9 in r)
print(list(range(11, 1000, 3)))
