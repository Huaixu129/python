# set
# 创建空set只能使用set方法
a = set()
# 可以用set()将列表转换成集合
b = set([1, 1, 2, 3])
print(b)
s = {2, 3, 4, 2}    # 集合中没有相同元素
print(s)    # {2, 3, 4}
# 向集合中添加元素
s.add(5)
print(s)    # {2, 3, 4, 5}
# 交集
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
print(a & b)    # {2, 3, 4}
print(a.intersection(b))
# 并集
print(a | b)    # {1, 2, 3, 4, 5}
print(a.union(b))
# 对称差
print(a ^ b)    # {1, 5}
print(a.symmetric_difference(b))
# 差
print(a-b)    # {1} a中元素减去b中相同元素
print(a.difference(b))
print(b-a)      # {5}
# 包含关系
b.issubset(a)   # 判断b是否是a的子集，返还bool，等效于 b <= a
a.issuperset(b)     # 判断a是否是b的父集，返还bool，等效于 a >= b

# 使用update, remove, pop 添加多个元素，删除，弹出元素
# 使用discard 删除元素，如果元素不存在不会报错

# 从a中去除所有属于b的元素
a.difference_update(b)
