'''
Author: CYLlinmaian
Date: 2022-07-25 12:00:02
LastEditTime: 2022-07-25 22:28:12
LastEditors: CYLlinmaian
Description: 
FilePath: \Python\18.列表.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
# 列表相当于其他语言中的数组

# 列表的创建
'''
列表需要使用[],元素和元素之间使用英文逗号进行分隔

# 列表的创建方式
    # 使用中括号
    # 调用内置函数list()
'''


from multiprocessing.sharedctypes import Value
from optparse import Values
from site import check_enableusersite
from tempfile import tempdir
from wordcloud import WordCloud
print('----------使用[]----------')
lst = ['hello', 'python', 21]
print(lst, lst[0], lst[1], lst[2])
print(id(lst), id(lst[0]), id(lst[1]), id(lst[2]))
print(type(lst), type(lst[0]), type(lst[1]), type(lst[2]))

print('----------使用list函数----------')
lst1 = list(['hello', 'python', 21])
print(lst1)
# @列表中元素的位置
print(lst1[0], lst1[-3])
print(lst1[1], lst1[-2])
print(lst1[2], lst1[-1])


# 列表的特点
'''
列表元素按照顺序有序排列
索引映射唯一个数据
列表可以存储重复数据
任意数据类型混存
根据需要动态分配和回收内存
'''

# 列表的操作
'''
#获取列表中指定元素的索引
    index()
        如查列表中存在N个相同元素,只返回相同元素中第一个元素的索引
        如果查询的元素在列表中不存在,则会抛出ValueError
        还可以在指定的start和stop之间进行查找
        
#获取列表中的单个元素
    正向索引从0到N-1    如lst[0]
    逆向索引从-N到-1    如lst[-N]
    指定索引不存在,抛出IndexError
    
#获取列表中的多个元素
    切片
        语法格式:列表名[start:stop:step]
        切片结果:原列表片段的拷贝
        切片范围:[start,stop]
        步长值step默认为1
        step为正数:从start开始往后计算切片
            [:stop:step]    切片的第一个元素默认是列表的第一个元素
            [start::step]   切片的最后一个元素默认是列表的最后一个元素
        step为负数:从start开始往前计算切片
            [:stop:step]    切片的第一个元素默认是列表的最后一个元素
            [start::step]   切片的最后一个元素默认是列表的第一个元素

#列表元素的查询操作
    #判断指定元素在列表中是否存在
        元素 in 列表名
        元素 nit in 列表名
    #列表元素的遍历
        for 迭代变量 in 列表名:
            相关操作

#列表元素的增加操作:向已存在的列表中增加新的元素
    方法:
        append()    在列表的末尾增加一个元素
        extend()    在列表的末尾至少添加一个元素
        insert()    在列表的任意位置添加一个元素
        切片    在列表的任意位置添加至少一个元素
    
#列表元素的删除操作:删除列表中已存在的元素
    方法:
        remove()
            一次删除一个元素
            重复元素只删除第一个
            元素不存在则抛出ValueError
        pop()
            删除一个指定索引位置上的元素
            指定索引不存在则抛出IndexError
            不指定索引则删除列表最后一个元素
        切片
            一次至少删除一个元素
        clear()
            清空列表
        del()
            删除列表
            
#列表元素的修改操作:①为指定索引的元素赋予一个新值;②为指定的切片赋予一个新值

#列表元素的排序操作:
    常见方法:
        调用sort()方法,列中所有的元素默认按照从小到大的顺序进行排序,可以指定reverse=True,进行降序排序,对原列表进行操作
        调用内置函数sorted(),可以指定reverse=True,进行降序排序,原列表不发生改变

#列表生成式:"生成列表的公式"
    语法格式:
        [i*i for i in range(1,10)]
    注意事项:
        "表示列表元素的表达式"中通常包含自定义变量
'''
# 获取索引
lst2 = ['Hello', 'World', 21, 'Hello']
print(lst2.index('Hello'))  # 有相同元素,只返回第一个元素的索引
print(lst2.index('World'))
'''print(lst2.index('world'))  #ValueError: 'world' is not in list'''
print(lst2.index('Hello', 1))
print(lst2.index('Hello', 1, 4))

# 单个元素
lst3 = ['Hello', 'World', 21, 'Hello', 'CYL', 'linmaian', 1314]
print(lst3[2])  # 获取索引为2的元素 正向索引
print(lst3[-3])  # 获取索引为-3的元素 逆向索引
'''print(lst3[11]) #IndexError: list index out of range'''

# 多个元素
lst4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = print(lst4[1:8])
x = print(lst4[1:8:])
b = print(lst4[1:8:2])
c = print(lst4[8:1:-2])
y = print(lst4[:8:])
y1 = print(lst4[:8:1])
y2 = print(lst4[:8:2])
z = print(lst4[1::])
z1 = print(lst4[1::1])
z2 = print(lst4[1::-1])
print(lst4[::-1])  # 逆序输出
print('原列表', id(lst4))
print('切片列表', id(a), id(b), id(c),
      id(x),
      id(y), id(y1), id(y2),
      id(z), id(z1), id(z2))

# 查询操作
lst5 = [10, 20, 'python', 'hello']
print(10 in lst5)
print(100 in lst5)
print(10 not in lst5)
print(100 not in lst5)  # 通过布尔值来判断元素是否存在于列表

print('------------------分割线------------------')
for item in lst5:
    print(item)

# 列表元素的添加
lst6 = [10, 20, 'python', 'hello', 'world']
print('增加元素之前', lst6, id(lst6))
lst6.append(100)
print('增加元素之后', lst6, id(lst6))
lst6.append(lst4)  # 将lst4作为一个元素添加到末尾
print(lst6)

lst7 = [1, 3, 5, 7, 9]
lst7.extend(lst4)  # 将lst4拆分单个元素后添加到末尾 一次性添加多个元素
print(lst7)

lst8 = [2, 4, 6, 8, 10]
lst8.insert(1, 'insert')
print(lst8)

lst9 = [True, False, 'hello']
lst6[4:] = lst9  # 相当于把切片下来的部分做一个替换
print(lst6)

lst10 = [0, 1, 2, 3, 4, 5, 3, 6, 7, 8, 9]
print(lst10)
lst10.remove(3)
print(lst10)
'''lst10.remove(100)   ValueError: list.remove(x): x not in list'''
lst10.pop(1)  # 指定元素索引
print(lst10)
'''lst10.pop(11)   IndexError: pop index out of range'''  # 超出了列表范围
lst10.pop()  # 不指定元素索引,默认删除列表最后一个元素
print(lst10)

new_lst = lst10[1:3]
print('原列表', lst10)
print('切片后的列表', new_lst)  # 产生了新的列表对象
lst10[1:3] = []  # 不产生新的列表
print(lst10)
lst10.clear()
print(lst10)
del lst10  # 对列表外部操作,所以不是lst.del
'''print(lst10)    NameError: name 'lst10' is not defined. Did you mean: 'lst1'?'''

# 元素修改
lst11 = [10, 20, 30, 40, 50]
print(lst11)
lst11[2] = 35
print(lst11)
lst11[1:3] = [200, 300, 400, 500]
print(lst11)

# 元素排序
lst12 = [34, 23, 45, 61, 27, 22, 57]
print('排序前的列表', lst12, id(lst12))
lst12.sort(reverse=False)   # 开始排序,调用列表对象sort方法,升序排序 也可以写成lst12.sort()
print('升序后的列表', lst12, id(lst12))
lst12.sort(reverse=True)  # 开始排序,降序排序
print('降序后的列表', lst12, id(lst12))

new_lst = sorted(lst12)
print('升序后的列表', new_lst, id(new_lst))  # 产生了一个新的列表
desc_lst = sorted(lst12, reverse=True)
print('降序后的列表', desc_lst, id(desc_lst))  # 产生了一个新的列表

# 列表公式
lst13 = [i*i for i in range(1, 11)]
print(lst13)
lst14 = [i*2 for i in range(1, 6)]
print(lst14)
