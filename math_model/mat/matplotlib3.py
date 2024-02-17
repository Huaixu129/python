import random

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# 引用中文字体
my_font = fm.FontProperties(fname="C:\Windows\Fonts\simsun.ttc", size=30)

y = [random.randint(0,3) for i in range(20)]
z = [random.randint(0,3) for i in range(20)]
x = [i for i in range(11,31)]

fig = plt.figure(figsize=(50,30),dpi=150)

# 设置x轴
_xtick_labels = ["{}岁".format(i) for i in range(11,31)]
plt.xticks(x, _xtick_labels, fontproperties=my_font, fontsize=60)
plt.yticks(range(0,4),fontsize=30)
# 设置信息h
plt.xlabel("年龄", fontproperties=my_font, fontsize=60)
plt.ylabel("女友个数",fontproperties=my_font, fontsize=60)
plt.title("11到30岁每年女友个数",fontproperties=my_font,color='r', fontsize=60)

# 设置网格
plt.grid(alpha=1) # alpha是透明度的意思


plt.plot(x,y, linewidth=5, label="自己", color='orange',linestyle=':') # linestyle有哪些需要用到的时候上网查
plt.plot(x,z, linewidth=5, label="同桌", color='cyan', linestyle='-')

# 添加图列
plt.legend(prop=my_font, fontsize=60, loc=0) # loc是图例的位置 borderpad是图例的大小

plt.show()