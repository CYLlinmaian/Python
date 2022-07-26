'''
Author: CYLlinmaian
Date: 2022-07-26 08:30:35
LastEditTime: 2022-07-26 09:07:01
LastEditors: CYLlinmaian
Description: 
FilePath: \Python\20.元组.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
# 元组:python内置的数据结构之一,是一个不可变序列
'''
#不可变序列与可变序列
    #不可变序列:字符串 元组
        没有增删改的操作
    #可变序列:列表 字典
        可以对序列执行增删改操作,对象地址不发生更改
'''

'''
#元组的创建方式
    #直接小括号:    t=('python','hello',90)
    #使用内置函数tuple():   t=tuple(('python','hello',90))
    #只包含一个元素的元组需要使用都好和小括号:  t=('hello',)  

#元组设计成不可变序列的原因
    #在多任务环境下,同时操作对象时不需要加锁
    
#注意事项!!!
    #元组中存储的是对象的引用
        如果元组中对象本身是不可变对象,则不能再引用其他对象
        如果元组中的对象是可变对象,则可变对象的引用不允许改变,但数据可以改变
'''
# 可变序列  增加后id不变
lst = [10, 20, 45]
print('增加前的id:', id(lst))
lst.append(300)
print('增加后的id:', id(lst))

# 不可变序列    增加后的id改变
s = 'hello'
print('增加前的id:', id(s))
s = s+'world'
print('增加后的id:', id(s))
print(s)


# 元组的创建
t = ('python', 'hello', 90)  # 小括号创建
print(t)
print(type(t))
t = tuple(('python', 'hello', 90))  # tuple创建
print(t)
print(type(t))
t = 'python', 'hello', 90  # 省略小括号
print(t)
print(type(t))
t = ('hello',)  # 一个元素的元组
print(t)
print(type(t))

'''空元组的创建'''
t = ()
print(t)
print(type(t))
t = tuple()
print(t)
print(type(t))
