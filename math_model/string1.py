# 字符串操作
# 字符串之间的相加相乘就是简单的拼接

# 分割 详细见demo1
line = "1 2 3 4 5"
numbers = line.split()
print(numbers)  # ['1', '2', '3', '4', '5']
# 连接
s = ' '
print(s.join(numbers))  # "1 2 3 4 5"
s = ','
print(s.join(numbers))  # "1,2,3,4,5"
# 替换 值替换，非引用替换
s = "hello world"
print(s.replace('world', 'python'))     # "hello python"
# 大小写转换
print(s.upper())    # "HELLO WORLD"
print(s.lower())    # "hello world"
"""
s.strip()返回一个将s两端的多余空格除去的新字符串。

s.lstrip()返回一个将s开头的多余空格除去的新字符串。

s.rstrip()返回一个将s结尾的多余空格除去的新字符串。
"""

"""
Python用字符串的`format()`方法来格式化字符串。
具体用法如下，字符串中花括号 `{}` 的部分会被format传入的参数替代，
传入的值可以是字符串，也可以是数字或者别的对象。
"""
m = '{color} {n} {x}'.format(n=10, x=1.5, color='blue')
print(m)    # blue 10 1.5
