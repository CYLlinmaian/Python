'''
Author: CYLlinmaian
Date: 2022-07-10 03:38:22
LastEditTime: 2022-07-10 03:41:04
LastEditors: CYLlinmaian
Description: 
FilePath: \Python\10.程序的组织结构-顺序结构.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
'''
计算机的流程控制
    顺序结构
        #程序从上到下顺序地执行代码，中间没有任何判断和跳转，直到程序结束
    选择结构    if语句
    循环结构    while语句 for-in语句
'''
# 实例：
# 顺序结构
'''把马西林打一顿需要几步'''
print('---程序开始---')
print('1、找到马西林')
print('2、和他面对面')
print('3、快速后仰迈开腿抬起脚向前用力')
print('4、然后给他一巴掌')
print('---程序结束---')

# python一切皆对象之对象的布尔值 所有的对象都会有一个布尔值True/False
# 对象布尔值:写代码的时候可以直接把对象放在条件表达式中去做判断
'''
以下对象的布尔值为False
    #False
    #数值0
    #None
    #空字符串
    #空列表
    #空元组
    #空字典
    #空集合
'''
# 测试对象的布尔值
print('------以下对象的布尔值为False------')
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(''))  # 空字符串
print(bool(""))  # 空字符串
print(bool([]))  # 空列表
print(bool(list()))  # 空列表
print(bool(()))  # 空元组
print(bool(tuple()))  # 空元组
print(bool({}))  # 空字典
print(bool(dict()))  # 空字典
print(bool(set()))
print(bool(False))
print(bool(False))
print(bool(False))
print(bool(False))
print('------其他对象的布尔值均为为Ture------')
