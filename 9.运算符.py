# 算术运算符
# 标准算术运算符
print(1 + 1)  # 加法运算
print(2 - 1)  # 减法运算
print(2 * 8)  # 乘法运算
print(11 / 2)  # 除法运算
print(11 // 2)  # 整除运算
print(11 % 2)  # 取余运算
print(2 ** 2)  # 表示2的2次方
print(2 ** 3)
# 取余运算符
# 幂运算符
# 拓展
print(9 // 4)
print(-9 // -4)
print(-9 // 4)  # !!!注意:一正一负整除时向下取整
print(9 // -4)

print(9 % 4)
print(-9 % -4)
print(-9 % 4)  # !!!注意:一正一负取余 余数=被除数-除数*商
print(9 % -4)

# 赋值运算符
'''赋值运算符的执行顺序是从右到左'''
i = 3 + 4
print(i)
a = b = c = 21  # 支持链式赋值
print(a, id(a))
print(b, id(b))
print(c, id(c))

# 支持参数赋值
a = 21
a += 32  # 相当于a=a+32
print(a, type(a))
a -= 11  # 相当于a=a-11
print(a, type(a))
a *= 2  # 相当于a=a*2
print(a, type(a))
a /= 4  # 相当于a=a/4
print(a, type(a))
a //= 2
print(a, type(a))

# 支持解包赋值
a, b, c = 11, 22, 33
print(a, b, c, type(a), type(b), type(c))

# 交换两个变量的值
a, b = 11, 22
print('交换之前', a, b)
a, b = b, a  # 交换 赋值交换
print('交换之后', a, b)

# 比较运算符
a, b = 11, 21
print('a>b吗?', a > b)
print('a<b吗?', a < b)
print('a>=b吗?', a >= b)
print('a<=b吗?', a <= b)
print('a==b吗?', a == b)
print('a==b吗?', a == b)
print('a!=b吗?', a != b)

'''
'='称为赋值运算符,'=='称为比较运算符
一个变量由三个部分组成:标识,类型,值
==比较的是值
对象的标识使用is来比较
'''
a = 11
b = 11
print(a == b)
print(a is b)
print(id(a), id(b))
print(a is not b)

# 拓展
lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst1 == lst2)
print(lst1 is lst2)
print(id(lst1), id(lst2))
print(lst1 is not lst2)

# 布尔运算符      与\或\非      and; or; not; in; not in
a, b = 1, 2
print(a == 1 and b == 2)  # 与的逻辑关系
print(a == 1 and b < 2)
print(a != 1 and b == 2)
print(a != 1 and b != 2)

print(a == 1 or b == 2)  # 或的逻辑关系
print(a == 1 or b < 2)
print(a != 1 or b == 2)
print(a != 1 or b != 2)

f = True  # 非的逻辑关系  取反
t = False
print(not f)
print(not t)

s='helloworld'
print('w' in s)
print('k' not in s)
print('w' not in s)
print('k' in s)



# 位运算符  将数据转成二进制进行计算

