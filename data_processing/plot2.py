import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 设置全局字体为 Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# 读取Excel文件
file_path = '../data/plotA.xlsx'
df_enzyme = pd.read_excel(file_path, sheet_name='enzyme')
df_gpcr = pd.read_excel(file_path, sheet_name='gpcr')
df_ic = pd.read_excel(file_path, sheet_name='ic')
df_nr = pd.read_excel(file_path, sheet_name='nr')

# 创建一个 2x2 的子图布局
fig, axs = plt.subplots(2, 2, figsize=(16, 16))  # 总图大小为 16x16
axs = axs.ravel()  # 将 2x2 的 axs 展平为一维数组，方便遍历

# 定义一个函数，用于绘制单个网络图
def plot_network(ax, df, title):
    # 创建一个无向图
    G = nx.Graph()

    # 遍历数据并添加边
    for _, row in df.iterrows():
        source = row['drug']
        target = row['target']
        G.add_edge(source, target)

    # 定义节点颜色
    node_colors = []
    for node in G.nodes:
        if node in df['drug'].values:
            node_colors.append('#7C7CBA')
        else:  # 否则是 target，设置为红色
            node_colors.append('#FFF0BC')


    # pos = nx.kamada_kawai_layout(G)  # 使用 Kamada-Kawai 布局
    pos = nx.circular_layout(G)      # 使用 Circular Layout（圆形布局）

    # 绘制节点和边
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors, node_size=1300)  # 绘制节点
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color='gray', width=2)  # 绘制边
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=10, font_weight='bold')  # 绘制节点标签

    # 设置标题，增大字体到 16
    ax.set_title(title, fontsize=18, fontweight='bold')  # 标题字体增大到 16
    ax.axis('off')  # 关闭坐标轴

# 绘制 4 个子图
plot_network(axs[0], df_enzyme, 'Enzyme')
plot_network(axs[1], df_gpcr, 'GPCRs')
plot_network(axs[2], df_ic, 'Ion Channel')
plot_network(axs[3], df_nr, 'Nuclear Receptor')

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()