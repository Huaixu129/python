# 初始化列表
# 无初始值
nums1: list[int] = []
# 有初始值
nums: list[int] = [1, 3, 2, 5, 4]

# 访问元素
num: int = nums[1]  # 访问索引 1 处的元素
# 更新元素
nums[1] = 0  # 将索引 1 处的元素更新为 0

# 清空列表
nums.clear()
# 尾部添加元素
nums.append(1)
nums.append(3)
nums.append(2)
nums.append(5)
nums.append(4)
# 中间插入元素
nums.insert(3, 6)  # 在索引 3 处插入数字 6
# 删除元素
nums.pop(3)  # 删除索引 3 处的元素
# 排序列表
nums.sort()  # 排序后，列表元素从小到大排列
