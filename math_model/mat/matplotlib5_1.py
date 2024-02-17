# 绘制纵向条形图

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

myFont = fm.FontProperties(fname="C:\Windows\Fonts\simsun.ttc", size=12)

a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇",
     "变形金刚5: 最后的骑士", "摔跤吧！爸爸", "加勒比海盗5: 死无对证",
     "金刚：骷髅岛", "极限特工: 终极回归", "生化危机6: 终章", "乘风破浪",
     "神偷奶爸3", "智取威虎山","大闹天竺","金刚狼3: 殊死一战","蜘蛛侠: 英雄归来",
     "悟空传","银河护卫队2","情圣","新木乃伊"]
b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61,
     11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88, 6.86, 6.58, 6.23]

plt.figure(figsize=(20,15), dpi=80)

_x = range(len(a))
plt.xticks(_x, a, fontproperties=myFont, rotation=45)
plt.bar(_x, b, width=0.3, color='orange')

plt.xlabel("电影名称",fontproperties=myFont, loc='right')
plt.ylabel("票房(单位:亿元)",fontproperties=myFont, loc='top')

# 在每个条形图上添加数值标签
for i, value in enumerate(b):
    plt.text(i, value + 0.1, '%.2f' % value, ha='center', va='bottom', fontproperties=myFont)
# value + 0.1: 表示在每个条形图上方 0.1 的位置添加数值标签。这个值可以根据需要调整，以确保标签不会与条形图重叠。

# 添加网格
plt.grid(alpha=0.7)

plt.show()