from numpy import array
from numpy import arange


def poly(x, a, b, c):
    y = a * x ** 2 + b * x + c
    return y


# 一般调用
print(poly(1, 1, 2, 3))  # 6
# 使用numpy数组
x1 = array([1, 2, 3])
print(poly(x1, 1, 2, 3))  # [ 6 11 18]
# 使用默认值参数
x2 = arange(10)  # 构建默认的numpy数组,长度为10
print(x2)  # [0 1 2 3 4 5 6 7 8 9]
print(poly(x2, 1, 2, 3))  # [  3   6  11  18  27  38  51  66  83 102]
