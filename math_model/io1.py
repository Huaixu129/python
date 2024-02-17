import os
# 写文件
"""
f = open('data.txt', 'w')
f.write('1 2 3 4\n')
f.write('2 3 4 5\n')
f.close()
"""
# 读文件

f = open("data.txt")
data = []
for line in f:
    data.append([int(filed) for filed in line.split()])
f.close()
print(data)     # [[1, 2, 3, 4], [2, 3, 4, 5]]

for row in data:
    print(row)
"""
[1, 2, 3, 4]
[2, 3, 4, 5]
"""
# 删除文件
"""
os.remove('data.txt')
"""
