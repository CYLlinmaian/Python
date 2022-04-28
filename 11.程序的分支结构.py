#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/26 21:52
# @Author  : CYLlinmaian
# @FileName: 11.程序的分支结构.py
# @Software: PyCharm

'''
程序的分支结构
    选择结构
        #程序根据判断条件的布尔值选择性地执行部分代码
    单分支结构
        #中文表达:如果．．．就．．．
        #语法结构:
            if 条件表达式
                条件执行体
    双分支结构   二选一执行
        #中文表达:如果是．．．不是就．．．
        #语法结构:
            if 条件表达式
                条件执行体1
            else:
                条件执行体2
    多分支结构   多选一执行,一般用来解决连续的区间段问题
        #中文表达:是．．．不是．．．
                是．．．不是．．．
                是．．．不是．．．
                是．．．不是．．．
                是．．．不是．．．
        #语法结构:
            if 条件表达式1
                条件执行体1
            elif 条件表达式2
                条件执行体2
            elif 条件表达式3
                条件执行体3
                .
                .
                .
            elif 条件表达式N
                条件执行体N
            [else:] #多分支结构中else可以省略
                条件执行体N+1
    嵌套if
        #语法结构:
        if 条件表达式1
            if 内层条件表达式
                内层条件执行体1
            else:
                内层条件执行体2
        else:条件执行体
'''
# 实例
# 单分支结构
money = 1000  # 余额
s = int(input('请输入取款金额:'))
if money >= s:
    money = money - s
    print('取款成功,余额为:', money)

# 双分支结构  if...else...
# 从键盘输入一个整数,判断其奇偶性
num = int(input("请输入要判断的整数:"))
if num % 2 == 0:
    print(num, '是偶数')
else:
    print(num, '是奇数')

#多分支结构,多选一执行
#从键盘录入一个存款整数,判断个人颜值等级
'''
90-100  A   亿表人才
80-89   B   翩翩公子
70-79   C   纸醉金迷
60-69   D   腰缠万贯
0-59    E   贫下中农
小于0或者大于100为非法数据(不是期待的有效值)
'''
score=int(input('请输入一个成绩:'))
if score>=90 and score<=100:
    print('亿表人才')
elif score>=80 and score<=89:
    print('翩翩公子')
elif score>=70 and score<=79:
    print('纸醉金迷')
elif score>=60 and score<=69:
    print('腰缠万贯')
elif score>=0 and score<=59:
    print('贫下中农')
else:
    print('对不起,这玩意不是个人')

#拓展 python中大于等于的另一种写法
score=int(input('请输入一个成绩:'))
if 90<=score<=100:
    print('亿表人才')
elif 80<=score<=89:
    print('翩翩公子')
elif 70<=score<=79:
    print('纸醉金迷')
elif 60<=score<=69:
    print('腰缠万贯')
elif 0<=score<=59:
    print('贫下中农')
else:
    print('对不起,这玩意不是个人')
    
    
#嵌套结构
'''
会员
    >=200 8折
    >=100 9折
    其他   不打折
非会员
    >=200 9.5折
    其他   不打折
'''
answer=input('您是会员吗?Y/N')
money=float(input('请输入您的购物金额:'))
if answer=='Y':
    if money>=200:
        print('尊敬的会员,您本次购物享受8折优惠,付款金额为:',money*0.8)
    elif money>=100:
        print('尊敬的会员,您本次购物享受9折优惠,付款金额为:',money*0.9)
    else:
        print('尊敬的会员,您本次购物的付款金额为:', money)
elif answer=='N':
    if money>=200:
        print('尊敬的顾客,您本次购物享受9.5折优惠,付款金额为:', money*0.95)
    else:
        print('尊敬的顾客,您本次购物的付款金额为:', money)
else:
    print('非法输入!!!')