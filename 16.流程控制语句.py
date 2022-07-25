'''
Author: CYLlinmaian
Date: 2022-07-10 18:50:07
LastEditTime: 2022-07-25 12:26:45
LastEditors: CYLlinmaian
Description: 
FilePath: \Python\16.流程控制语句.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''

# break语句
# 用于结束循环,通常与分支结构if一起使用
'''从键盘录入密码，最多输三次，密码正确结束循环'''

for item in range(3):
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')


a = 0
while a < 3:
    '''条件执行体(循环体)'''
    pwd = input('请输入密码:')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确!!!')

        '''改变变量'''
    a += 1


# continue语句
# 用于结束当前循环,进入下一次循环,通常与分支结构中的if一起使用
'''要求输出1~50之间所有5的倍数'''
'''
分析:5的倍数的共同点:和5的余数为0的数都是5的倍数
什么样的数不是5的倍数:与5的余数不为0的数都不是5的倍数
'''
print('-----------------常规方法-----------------')
for item in range(1, 51):
    if item % 5 == 0:
        print(item)


print('-----------------使用continue语句------------------')
for item in range(1, 51):
    if item % 5 != 0:
        continue
    print(item)


# else语句
for item in range(3):
    pwd = input('请输入密码:')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')

else:
    print('警告,密码三次输入错误,系统将在30s后启动自毁程序!!!')


a = 0
while a < 3:
    pwd = input('请输入密码:')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    '''改变变量'''
    a += 1

else:
    print('警告,密码三次输入错误,系统将在30s后启动自毁程序!!!')
