# dictionary
# 字典本质是键值对
d = {'dogs': 5, 'cats': 4}
# 查
print(d['dogs'])
# 增
d['pig'] = 3
# 改
d['cats'] = 2
# 所有键
print(d.keys())     # dict_keys(['dogs', 'cats', 'pig'])
# 所有值
print(d.values())   # dict_values([5, 2, 3])
# 所有键值对
print(d.items())    # dict_items([('dogs', 5), ('cats', 2), ('pig', 3)])
# 创建空字典 两种方法
a = {}
b = dict()
inventory = dict(
    [('foozelator', 123),
     ('frombicator', 18),
     ('spatzleblock', 34),
     ('snitzelhogen', 23)
    ])  # 使用dict初始化字典
# 使用元组作为键
connections = {('New York', 'Seattle'): 100, ('Austin', 'New York'): 200, ('New York', 'Austin'): 400}
# 使用get方法查看值，若无该键值对，返回none，不会报错
print(inventory.get('foozelator'))  # 123
print(connections.get(('chengdu', 'wuhan')))    # None
# 使用pop删除键值对
print(inventory.pop('frombicator'))     # 18 若键值对不存在则报错
# 使用del删除
del inventory['snitzelhogen']
# 使用update更新/添加键值对
person = {'first': "James", 'last': "Maxwell", 'born': 1831}
person_modifications = {'first': 'James', 'middle': 'Clerk'}
person.update(person_modifications)     # 相同则修改，不同则添加
# 判断语句
print('first' in person)    # True

# `keys` 方法，`values` 方法和`items` 方法 返还列表
print(person.keys())    # dict_keys(['first', 'last', 'born', 'middle'])
