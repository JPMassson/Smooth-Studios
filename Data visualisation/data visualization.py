import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

opacity = 0.8
colors = ['b', 'g', 'r', 'y']

df = pd.read_csv(r'C:\Users\王冲\Desktop\DataCSV.csv')

df.fillna(0, inplace=True)

# 定义技能列表
skills = ['first technical skill', 'second technical skill', 'first non-technical skill', 'second non-technicalskill']

# 创建数据库连接
# conn = sqlite3.connect('database.db')


# 从数据库中读取数据并转换为 Pandas 数据帧
# df = pd.read_sql('SELECT * FROM mytable', conn)
# 创建空字典来存储技能计数
skill_counts = {}

# 遍历每个技能类别
for skill in skills:
    # 获取该技能类别下的所有技能
    all_skills = df[skill].unique()
    # 计算每个技能的数量
    counts = df[skill].value_counts().sort_index()
    # 存储技能计数到字典中
    skill_counts[skill] = counts

# 确定柱状图的宽度和位置
num_skills = max(len(counts) for counts in skill_counts.values())
bar_width = 0.2
index = np.arange(num_skills)

# 创建柱状图
fig, ax = plt.subplots()

# 遍历每个技能类别并绘制柱状图
for i, skill in enumerate(skills):
    # 获取技能计数
    counts = skill_counts[skill]
    # 获取技能名称
    skill_names = counts.index
    # 获取计数值
    count_values = counts.values

    # 将技能计数值对齐到柱状图的位置
    aligned_values = np.zeros(num_skills)
    aligned_values[:len(count_values)] = count_values

    # 在对应位置绘制柱状图
    bar = ax.bar(index + i * bar_width, aligned_values, bar_width, alpha=opacity, color=colors[i], label=skill)

    # 在柱状图上添加计数值标签
    for rect in bar:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height, f'{height}', ha='center', va='bottom')

plt.xlabel('Skills')
plt.ylabel('Counts')
plt.title('Skills Counts by Person')
plt.xticks(index + bar_width * (len(skills) - 1) / 2, skill_names)
plt.legend()

plt.tight_layout()
plt.show()