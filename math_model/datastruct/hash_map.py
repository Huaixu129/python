# 初始化哈希表
hmap: dict = {12836: " 小哈", 15937: " 小啰", 16750: " 小算", 13276: " 小法", 10583: " 小鸭", 10212: "小坏"}
# 添加操作
# 在哈希表中添加键值对 (key, value)
# hmap[12836] = " 小哈"
# 查询操作
# 向哈希表输入键 key ，得到值 value
name: str = hmap[15937]
# 删除操作
# 在哈希表中删除键值对 (key, value)
hmap.pop(10583)

# 遍历哈希表
# 遍历键值对 key->value
for key, value in hmap.items():
    print(key, "->", value)
# 单独遍历键 key
for key in hmap.keys():
    print(key)
# 单独遍历值 value
for value in hmap.values():
    print(value)
