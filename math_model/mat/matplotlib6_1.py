# # 未统计的数据才能绘制直方图，统计过的数据只能绘制条形图
#
# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
#
# my_font = fm.FontProperties(fname="C:\Windows\Fonts\simsun.ttc")
#
# interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
# width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
# quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]
#
# plt.bar(range(len(quantity)),quantity,width=1)
#
# # 设置X轴刻度
# _x = [i-0.5 for i in range(12+1)]
# plt.xticks(_x,interval+[150])
#
# plt.grid(alpha=0.3)
# plt.show()
