import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置全局字体为 Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 15  # 设置默认字体大小

# 读取 Excel 文件中的 Sheet1A
file_path = '../data/plot.xlsx'
data_enzyme = pd.read_excel(file_path, sheet_name='enzyme')
data_gpcr = pd.read_excel(file_path, sheet_name='gpcr')
data_ic = pd.read_excel(file_path, sheet_name='ic')
data_nr = pd.read_excel(file_path, sheet_name='nr')

# 创建一个 2x2 的 figure
fig, axes = plt.subplots(2, 2, figsize=(15, 12))


# 定义绘制 CDF 图的函数
def plot_cdf(ax, data, title):
    sorted_rank = np.sort(data['rank'])
    yvals = np.arange(len(sorted_rank)) / float(len(sorted_rank))
    ax.plot(sorted_rank, yvals, color='purple', label='CDF')

    # 定义累积概率阈值
    thresholds = [0.50, 0.70, 0.90]
    colors = ['blue', 'orange', 'red']

    # 找到累积概率达到 50%, 70%, 90% 时的排名值
    for threshold, color in zip(thresholds, colors):
        rank_at_threshold = sorted_rank[np.searchsorted(yvals, threshold)]
        # 添加垂直线和水平线，标记阈值位置
        ax.axvline(x=rank_at_threshold, color=color, linestyle='--',
                   label=f'{int(threshold * 100)}% Rank: {rank_at_threshold:}')
        ax.axhline(y=threshold, color=color, linestyle='--', label=f'Cumulative Probability: {threshold:.2f}')
        # 添加注释
        ax.text(rank_at_threshold + 0.05 * max(sorted_rank), threshold - 0.05,
                f'{int(threshold * 100)}% at Rank: {rank_at_threshold:}', fontsize=12, color=color)

    # 计算原始数据的平均值和中位数
    mean_rank = np.mean(data['rank'])
    median_rank = np.median(data['rank'])

    # 将平均值和中位数添加到图例中
    ax.plot([], [], ' ', label=f'Mean Rank: {mean_rank:.2f}')  # 添加空行用于图例
    ax.plot([], [], ' ', label=f'Median Rank: {median_rank:.2f}')  # 添加空行用于图例

    # 设置图表标题和标签
    ax.set_title(title, fontsize=20, fontweight='bold')
    ax.set_xlabel('Rank', fontsize=15)
    ax.set_ylabel('Cumulative Probability', fontsize=15)
    ax.grid(True)
    ax.legend(fontsize=12)


# 绘制 enzyme CDF 图
plot_cdf(axes[0, 0], data_enzyme, 'Enzyme (test samples:100 total samples:292579)')

# 绘制 gpcr CDF 图
plot_cdf(axes[0, 1], data_gpcr, 'GPCRs (test samples:98 total samples:20417')

# 绘制 ic CDF 图
plot_cdf(axes[1, 0], data_ic, 'Ion Channel (test samples:100 total samples:41498)')

# 绘制 nr CDF 图
plot_cdf(axes[1, 1], data_nr, 'Nuclear Receptor (test samples:25 total samples:1074)')

# 调整子图间距
plt.tight_layout()
plt.show()