'''
Author: CYLlinmaian
Date: 2022-07-10 03:38:22
LastEditTime: 2022-07-23 12:48:44
LastEditors: CYLlinmaian
Description: 
FilePath: \Python\6.python中常见数据类型.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
# 整数类型：不带小数点，不带单引号-->int 98 正数、复数、零
# 可以表示为二进制、十进制（默认）、八进制、十六进制
from decimal import Decimal
n1 = -1
n2 = 0
n3 = 1
print(n1, n2, n3, )
print(type(n1), type(n2), type(n3))
print('十进制', 121)
print('二进制', 0b11011001011)
print('八进制', 0o176)
print('十六进制', 0x1EAF)

# 浮点数类型：带小数点的-->float 3.1415926
a = 3.1415926
print(a, type(a))
a1 = 1.1
a2 = 2.2
a3 = 3.3
print(a1 + a2)
print(a1 + a3)
'''计算不精确的问题不是所有小数都出现，只有部分会出现'''

print(Decimal('1.1') + Decimal('2.2'))
print(Decimal(a1) + Decimal(a2))

# 布尔类型：只有两-->bool True/False
'''python中的布尔类型可以转成整数进行计算，首字母必须大写'''
f1 = True
f2 = False
print(f1, f2)
print(type(f1), type(f2))
print(f1 + 1)  # 2  1+1的结果为2，True表示1
print(f2 + 1)  # 1  0+1的结果为1，False表示0

# 字符串类型：汉字啥的-->str 人生苦短
'''又称为不可变的字符序列
可以使用单引号‘ ’、双引号“ ”、三引号’‘’ ‘’‘、或者“”“ ”“”来定义
单引号和双引号定义的字符串必须在一行
三引号定义的字符串可以分布在连续的多行'''
str1 = '人生苦短'
str2 = "人生苦短"
str3 = """人生
        苦短"""
str4 = '''人生
        苦短'''
print(str1, str2, str3, str4)
print(type(str1), type(str2), type(str3), type(str4))
