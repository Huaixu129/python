# 显示每个时间点对应的温度
import random
import matplotlib

from matplotlib import matplotlib as fm
from matplotlib import matplotlib as plt

# windows linux 设置字体方式
# font = {                                                # 这个方法不能用于设置颜色
#         'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 20,
# }
# matplotlib.rc('font', **font)

# 三种操作系统通用设置字体方法，必须在坐标设置方法中引用
my_font = fm.FontProperties(fname="C:\Windows\Fonts\simsun.ttc")

x = range(0, 120)
y = [random.randint(20, 37) for i in range(120)]  # 构造随机数列表方法

fig = plt.figure(figsize=(20, 10), dpi=100)

plt.plot(x, y,color='r')

# 调整X轴刻度
_x = list(x)[::6]  # 设置X轴步长
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(_x, _xtick_labels[::6], rotation=45, fontproperties=my_font)  # 取步长必须一一对应,rotation表示逆时针中心旋转多少度

# 添加描述信息
plt.xlabel("时间", fontproperties=my_font, color='skyblue')
plt.ylabel("温度", fontproperties=my_font)
plt.title("十点到十二点每分钟的气温变化情况", fontproperties=my_font)
plt.show()
