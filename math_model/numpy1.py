# numpy array
from matplotlib.pyplot import plot

from math1 import pi

from numpy import array, linspace
import numpy as np
a = array([1, 2, 3, 4])
b = a + 2
print(b)    # [3 4 5 6]
c = a + a
print(c)    # [2 4 6 8]
c.shape = 2, 2
print(c)    # [[2 4] [6 8]]
print(c + c)    # [[ 4  8] [12 16]]
a = linspace(0, 2*pi, 21)  # 表示在0 ~ 2pi生成21段数据
print(a)
b = np.sin(a)
print(b)
plot(a, b)

