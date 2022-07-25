'''
Author: CYLlinmaian
Date: 2022-07-25 22:33:35
LastEditTime: 2022-07-26 01:16:34
LastEditors: CYLlinmaian
Description:
FilePath: \Python\19.字典.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
'''
# 什么是字典?
    # python内置的数据结构之一,与列表一样是一个可变序列
    # 以键值对的方式存储数据,字典是一个无序的序列
    
# 字典的实现原理
    # 字典的实现原理与查字典类似,根据key值查找value所在的位置
    
# 字典的创建
    # 使用花括号,最常用:
        scores={'张三':100,'李四':98,'王五',59}
    # 使用内置函数dict()
        dict(name ='jack',age=20)
    #字典生成式    
        
# 字典的常用操作
    # 字典中元素的获取
        # [] 举例:scores['张三']
            如果字典中不存在指定的key,抛出KeyError异常
        # get()  举例:scores.get('张三')
            如果字典中不存在指定的key,并不会抛出KeyError而是返回None,可以通过参数设置默认的value,以便指定的key不存在时返回
    # 字典的增删查改
    # 字典的视图操作
        # keys() 获取字典中所有的键
        # values()   获取字典中所有的value
        # items()    获取字典中所有key-value对
    #字典元素的遍历:依次获取字典中的元素
        for item in scores:
    #字典的特点:
        #字典中的所有元素都是一个key-value对,其中key不允许重复,value可以重复
        #字典中的元素是无序的
        #字典中的key必须是不可变对象
        #字典也可以根据需要动态的伸缩
        #字典会浪费大量的内存,是一种使用空间换时间的数据结构
    #字典生成式:生成字典的公式
        #内置函数zip()
            用于将可迭代对象作为参数,将对象中对应的元素打包成一个元组,然后返回由这些元组组成的列表
                {item.uppper():price for item,price in zip(item,prices)}
'''
# 字典的创建


from optparse import Values
from typing import ValuesView
scores = {'张三': 100, '李四': 98, '王五': 59}  # 使用{}创建字典
print(scores)
print(type(scores))

student = dict(name='jack', age=20)  # 使用内置函数创建字典
print(student)
print(type(student))

d = {}  # 创建空字典
print(d)
print(type(d))

# 元素的获取
print(scores['张三'])  # []获取元素
'''print(scores['李六'])   #KeyError: '李六' '''

print(scores.get('张三'))  # get()获取元素
print(scores.get('李六'))  # 返回None
print(scores.get('麻七', 99))  # 99是在查找'麻七'所对的value不存在时,提供的一个默认值

# Key的判断
print('张三' in scores)
print('张三' not in scores)

# 字典元素的删除
del scores['张三']  # 删除指定的key-value对
print(scores)
'''
scores.clear()  #清空字典的元素
print(scores)
'''

# 字典元素的增加
scores['陈六'] = 99
print(scores)

# 字典元素的修改
scores['陈六'] = 100
print(scores)

# 获取所有的key
keys = scores.keys()
print(type(keys))
print(keys)
print(list(keys))  # 将所有的键转成列表

# 获取所有的value
values = scores.values()
print(type(values))
print(values)
print(list(values))

# 获取所有的key-values对
items = scores.items()
print(items)
print(list(items))  # 转换之后的列表元素是由元组组成的

# 字典元素的遍历
for item in scores:
    print(item, scores[item], scores.get(item))

# 字典的特点
d = {'name': '张三', 'name': '李四'}  # key不允许重复
print(d)

d = {'name': '张三', 'nickname': '张三'}  # value可以重复
print(d)

# 字典生成式
items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 89]

d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
