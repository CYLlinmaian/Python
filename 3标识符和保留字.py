'''
Author: CYLlinmaian
Date: 2022-07-10 03:38:22
LastEditTime: 2022-07-10 03:39:00
LastEditors: CYLlinmaian
Description: 
FilePath: \Python\3标识符和保留字.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
import keyword

print(keyword.kwlist)
print(keyword.iskeyword('is'))

# 规则：
#   字母 数字 下划线
#   不能以数字开头
#   不能保留字
#   严格区分大小写
