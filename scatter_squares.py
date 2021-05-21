import matplotlib.pyplot as plt

plt.style.use('seaborn')
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)
# 设置图标标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小--set-upstream 15SCSJ dev
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()