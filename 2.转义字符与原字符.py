print('hello\nworld')    #转义功能的首字母  n-->newline的首字母表示换行
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')   #回车符，world覆盖了hello
print('hello\bworld')   #退一个格，o没了

print('http:\\\\www.baidu.com')

print('老师说:\'你好\'')

#原字符，不希望字符串中的转义字符起作用，就使用原字符，在字符串之前加上r或者R
print(r'hello\nworld')
#！！！注意：最后一个字符不能是单数的反斜杠
#print(r'hello\nworld\')
print(r'hello\nworld\\')