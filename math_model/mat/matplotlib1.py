# import matplotlib.pyplot as plt
#
# fig = plt.figure(figsize=(50, 30), dpi=100)
# X = range(2, 26, 2)
# Y = [12, 23, 24, 25, 26, 32, 37, 35, 26, 27, 19, 10]
# plt.plot(X, Y)
# # plt.savefig("./fig_save.svg")   # 保存图片
# plt.xticks(X, fontsize=40)  # 设置X轴
# plt.yticks(range(min(Y), max(Y)+1, 2), fontsize=40)  # 设置Y轴 fontsize是坐标尺寸
# plt.show()
import numpy as np
import plotly.graph_objects as go

# 模拟三月每天的温度，呈现上升趋势
march_temperatures = np.linspace(10, 25, 31) + np.random.normal(0, 3, 31)

# 模拟十月每天的温度，呈现下降趋势
october_temperatures = np.linspace(25, 15, 31) + np.random.normal(0, 3, 31)

x_1 = range(1,32)
x_2 = range(51,82)

# 创建散点图
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=list(x_1),
    y=march_temperatures,
    mode='markers',
    name='三月份'
))

fig.add_trace(go.Scatter(
    x=list(x_2),
    y=october_temperatures,
    mode='markers',
    name='十月份'
))

# 调整X轴刻度
_x = list(x_1) + list(x_2)
_xtick_labels = ["三月{}号".format(i) for i in range(1,32)] + ["十月{}号".format(i) for i in range(1,32)]
fig.update_xaxes(tickvals=_x[::3], ticktext=_xtick_labels[::3])

# 添加标识
fig.update_layout(
    title="三月和十月每日温度散点图",
    xaxis_title="时间",
    yaxis_title="温度(单位:摄氏度)",
    legend_title="月份",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)

fig.show()