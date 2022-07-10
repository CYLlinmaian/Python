'''
Author: CYLlinmaian
Date: 2022-07-10 03:38:22
LastEditTime: 2022-07-10 20:20:41
LastEditors: CYLlinmaian
Description: 
FilePath: \Python\15.程序的循环结构.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''

'''
循环结构
    #反复做同一件事情的情况,称为循环
    #循环结构的分类
        ①while
        ②for -in
    #while循环的语法结构
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
for-in循环
    in表达从(字符串、序列等)中依次取值，又称为遍历
    for-in便利的对象必须是可迭代对象
    #for-in循环的语法结构
        for 自定义的变量 in 可迭代对象:
            循环体
    循环体内不需要访问自定义变量，可以将自定义变量替代为下划线
'''


# 实例
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
sum = 0
a = 0
while a < 101:
    sum += a
    a += 1
print('0到100的和为:', sum)
# !!!警告,注意缩进,不要将print写入循环

# 练习 计算1到100之间的偶数和
sum = 0
a = 1
while a <= 100:
    if a % 2 == 0:  # 'if a%2:'奇数和条件
        sum += a
    a += 1
print('1~100之间的偶数和为:', sum)

# for-in循环
for item in 'python':  # 依次遍历，依次取出p、y、t、h、o、n并打印输出
    print(item)

for i in range(10):  # range()函数也是一个可迭代对象
    print(i)

# 如果在循环体中不想需要使用到自定义变量,可以将自定义变量写为"_"
for _ in range(5):
    print('人生苦短,及时行乐!!!')

# 使用for循环计算1到100之间的偶数和
sum = 0
for item in range(1, 101):
    if item % 2 == 0:
        sum += item
print('1到100之间的偶数和为:', sum)
