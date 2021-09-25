import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 创建一个RandomWalk实例，并将其所有包含的点都绘制出来
rw = RandomWalk(500)
rw.fill_walk()

#  设置绘图窗口尺寸
plt.figure(figsize=(10, 6))

#  隐藏坐标轴
current_axes = plt.axes()
current_axes.xaxis.set_visible(False)
current_axes.yaxis.set_visible(False)

point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, color='g', linestyle='solid', linewidth=0.5)

#  突出起点和终点
plt.scatter(0, 0, c='green', edgecolor='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

#  显示图形
plt.show()
