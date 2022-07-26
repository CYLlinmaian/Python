'''
Author: CYLlinmaian
Date: 2022-07-26 09:55:19
LastEditTime: 2022-07-26 16:16:21
LastEditors: CYLlinmaian
Description:
FilePath: \Python\21.集合.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
# 集合:python语言提供的内置数据结构;与列表 字典一样都属于可变类型的序列;集合是没有value的字典
'''
# 集合的创建方法
    # 直接{}
        s={'python','hello',90}
    # 调用内置函数set()

#集合的相关操作
    #集合元素的判断操作
        in或not in
    #集合元素的新增操作
        调用add()方法,一次添加一个元素
        调用update()方法,至少添加一个元素
    #集合元素的删除操作
        调用remove()方法,一次删除一个指定元素,如指定的元素不存在则抛出KeyError
        调用discard()方法,一次删除一个指定元素.如果指定的元素不存在不抛出异常
        调用pop()方法,一次只删除一个任意元素
        调用clear()方法,清空集合

#集合之间的关系
    #两个集合是否相等
        可以使用运算符==或者!=进行判断
    #一个集合是否是另一个集合的子集
        可以调用方法issubset进行判断
        B是A的子集
    #一个集合是否是另一个集合的超集
        可以调用方法issuperset进行判断
        A是B的超集
    #两个集合是否没有交集
        可以调用方法isdisjoint进行判断
        
#集合的数学操作
    #交集
    #并集
    #差集
    
#集合生成式:用于生成集合的公式
    #{i*i for i in range(1,10)}
    #将{}改为[]就是列表生成式
    #没有元组生成式(元组是唯一个不可变序列)
'''
# 集合的创建
# {2, 3, 4, 5, 6, 7, 8, 9, 10, 11} #集合中的元素不允许重复


s = {2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 10, 11, 11, 11}
print(s)

s1 = set(range(6))
print(s1, type(s1))
s2 = set([1, 2, 3, 4, 5, 6, 6, 7, 8])
print(s2, type(s2))
s3 = set((12, 32, 34, 54, 65, 76, 76, 97, 98))  # 集合中的元素是无序的
print(s3, type(s3))
s4 = set('python')
print(s4, type(s4))
s5 = set({12, 34, 54, 67, 788, 54, 45, 34})
print(s5, type(s5))

# 创建一个空集合
s6 = set()
print(type(s6))

# 集合的操作
#   判断操作
s7 = {10, 20, 30, 45, 550, 987}
print(10 in s7)
print(100 in s7)
print(10 not in s7)
print(100 not in s7)
#   新增操作
s7.add(57)
print(s7)

s7.update({200, 300, 400})
print(s7)
s7.update([23, 32, 47])
print(s7)
s7.update((240, 350, 470))
print(s7)

#   删除操作
s7.remove(240)
print(s7)
'''s7.remove(500)  #KeyError: 500'''
s7.discard(400)
print(s7)
s7.discard(400)  # 400已经不存在 未抛异常
print(s7)
s7.pop()  # 不能指定参数,随即删除
print(s7)
s7.clear()  # 清空集合元素
print(s7)

# 集合之间的关系
sx = {10, 20, 30, 40, 50, 60, 70, 80}
sy = {10, 20, 30, 40, 50}
sz = {10, 20, 100}
print(sy.issubset(sx))
print(sz.issubset(sx))
print(sx.issuperset(sy))
print(sx.issuperset(sz))
print(sy.isdisjoint(sz))  # 有交集为False,无交集为True

# 集合的数学操作
#   交集
print(sy.intersection(sx))
print(sy.intersection(sz))
print(sx & sy)  # &求交集 与intersection()方法等价
#   并集
print(sx.union(sy))
print(sz.union(sy))
print(sx | sy)  # |求并集 与union()方法等价
#   差集
print(sx.difference(sy))
print(sx - sy)  # -求差集 与difference()方法等价
print(sx.symmetric_difference(sy))
print(sx ^ sy)  # ^求对称差集 与sysmmetric_difference()方法等价

# 集合生成式
print([i*i for i in range(1, 11)])  #列表生成式
print({i*i for i in range(1, 11)})  #集合生成式
