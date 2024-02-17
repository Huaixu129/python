# list
# list的生成 两种方法
empty_list1 = []
empty_list2 = list()
# 分割字符串
s = "hello world"
print(s.split())  # 以空格为分隔符 ['hello', 'world']
p = "welcome to CCNU"
"""下面这行也可以写成 split(p," ",3) 数字表示分成的块数 第二个元素表示分割的flag且不保留flag"""
print(p.split("c", 3))  # ['wel', 'ome to CCNU']
# 列表的加法
m = s.split() + p.split()
print(m)  # ['hello', 'world', 'welcome', 'to', 'CCNU']
# 增加列表元素
m.append("haha")
print(m)    # ['hello', 'world', 'welcome', 'to', 'CCNU', 'haha']
# 删除列表元素
del m[5]
print(m)    # ['hello', 'world', 'welcome', 'to', 'CCNU']
# 判断从属关系
s = 'hello world'
print('hel' in s)   # True
print('o w' not in s)   # False

# list 方法
a = [11, 12, 13, 12, 11]

b = a.count(11)     # 返回出现次数
print(b)

c = a.index(12)       # 返还索引，未找到报错
print(c)

a.extend([18, 19])   # 在末尾插入列表
print(a)    # [11, 12, 13, 12, 11, 18, 19]

a.insert(3, [15])  # 在指定位置插入元素
print(a)    # [11, 12, 13, [15], 12, 11, 18, 19]

a.remove([15])  # 移除元素
print(a)    # [11, 12, 13, 12, 11, 18, 19]

print(a.pop(2))     # `l.pop(idx)` 会将索引 `idx` 处的元素删除，并返回这个元素

a.sort()    # 这个sort是直接改变原列表
print(a)    # 从小到大排
e = sorted(a)   # 拷贝原列表

a.reverse()     # 列表转向，直接改变原列表
f = a[0:0:-1]   # 拷贝原列表
