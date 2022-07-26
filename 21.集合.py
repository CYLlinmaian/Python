'''
Author: CYLlinmaian
Date: 2022-07-26 09:55:19
LastEditTime: 2022-07-26 11:14:29
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
