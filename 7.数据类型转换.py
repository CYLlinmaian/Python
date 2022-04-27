'''将不同数据类型的数据拼接在一起'''
name='小林'
age=20
year='00'
print(type(name),type(age),type(year))
#不同数据类型直接输出时会报错,需使用类型转换str来进行连接
print('我叫'+name+'今年'+str(age)+'岁'+'是一个'+year+'后')


print('---------------str()将其他类型转成str类型----------------')
a=1314
b=13.14
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c))


print('---------------int()将其他类型转成int类型----------------')
a=1314
b=13.14
c=False
d=True
e=0x689
print(type(a),type(b),type(c),type(d),type(e))
print(int(a),int(b),int(c),int(d),int(e))
'''将str转成int类型,字符串为数字串
    将float转成int类型,只保留整数部分
    将str转成int类型报错的原因:字符串必须为数字且是字符串不能为小数串'''



print('---------------float()将其他类型转成float类型----------------')
a='1314'
b='13.14'
c=False
d=True
e=0x567
print(type(a),type(b),type(c),type(d),type(e))
print(float(a),float(b),float(c),float(d),float(e))
'''字符串中的数据如果是非数字串,则不允许转换'''

#程序运行结果如下
'''
我叫小林今年20岁是一个00后
---------------str()将其他类型转成str类型----------------
<class 'int'> <class 'float'> <class 'bool'>
1314 13.14 False
---------------int()将其他类型转成int类型----------------
<class 'int'> <class 'float'> <class 'bool'> <class 'bool'> <class 'int'>
1314 13 0 1 1673
---------------float()将其他类型转成float类型----------------
<class 'str'> <class 'str'> <class 'bool'> <class 'bool'> <class 'int'>
1314.0 13.14 0.0 1.0 1383.0
'''