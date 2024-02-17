# 对比数据版的条形图

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 字体设置
myFont = fm.FontProperties(fname="C:\Windows\Fonts\simsun.ttc", size=12)

# 图片尺寸
plt.figure(figsize=(20,15), dpi=80)

# 数据
a = ["猩球崛起3: 终极之战", "敦刻尔克", "蜘蛛侠: 英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

barWidth = 0.2
x_14 = list(range(len(a)))
x_15 = [i+barWidth for i in x_14]
x_16 = [i+barWidth*2 for i in x_14]

# 设置x轴
_x = range(len(a))
plt.xticks(x_15,a,fontproperties=myFont,rotation=0)

# 绘制条形图
plt.bar(_x, b_14, width=barWidth, color='orange', label="9月14日")
plt.bar(x_15, b_15, width=barWidth, color='skyblue', label="9月15日")
plt.bar(x_16, b_16, width=barWidth, color='red', label="9月16日")

# 在每个条形图上添加数值标签
for i, value in enumerate(b_14):
    plt.text(i, value + 0.1, str(value), ha='center', va='bottom', fontproperties=myFont)

for i, value in enumerate(b_15):
    plt.text(i + barWidth, value + 0.1, str(value), ha='center', va='bottom', fontproperties=myFont)

for i, value in enumerate(b_16):
    plt.text(i + barWidth * 2, value + 0.1, str(value), ha='center', va='bottom', fontproperties=myFont)

#设置坐标信息
plt.xlabel("电影名称",fontproperties=myFont, loc='right')
plt.ylabel("票房(单位:万元)",fontproperties=myFont, loc='top')

# 添加网格
plt.grid(alpha=0.7)

# 添加图例
plt.legend(prop=myFont, fontsize=60, loc=0)

# 展示
plt.show()