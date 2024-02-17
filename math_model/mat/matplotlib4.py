
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

my_font = fm.FontProperties(fname="C:\Windows\Fonts\simsun.ttc", size=12)

# 模拟三月每天的温度，呈现上升趋势
march_temperatures = np.linspace(10, 25, 31) + np.random.normal(0, 3, 31)

# 模拟十月每天的温度，呈现下降趋势
october_temperatures = np.linspace(25, 15, 31) + np.random.normal(0, 3, 31)

x_1 = range(1,32)
x_2 = range(51,82)

plt.figure(figsize=(20,8), dpi=80)

# 绘制散点图
plt.scatter(x_1,march_temperatures, label="三月份")
plt.scatter(x_2,october_temperatures, label="十月份")

# 调整X轴刻度
_x = list(x_1) + list(x_2)
_xtick_labels = ["三月{}号".format(i) for i in range(1,32)] + ["十月{}号".format(i) for i in range(1,32)]
plt.xticks(_x[::3],_xtick_labels[::3],rotation=45, fontproperties=my_font)

# 添加标识
plt.xlabel("时间", fontproperties=my_font,loc='right')
plt.ylabel("温度(单位:摄氏度)", fontproperties=my_font,loc='top')
plt.title("三月和十月每日温度散点图", fontproperties=my_font)

# 添加图例
plt.legend(prop=my_font, fontsize=60, loc=0)

plt.show()