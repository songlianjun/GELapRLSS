import pandas as pd
import random

def data_split(path):
    # 读取Excel文件
    file_path = path
    xls = pd.ExcelFile(file_path)

    # 读取 interaction sheet 内容
    df_interaction = xls.parse("A")

    # 1. 生成所有的组合名称（用"-"分隔）和对应的数值
    combinations = []
    for index, row in df_interaction.iterrows():
        compound = row.iloc[0]  # 第一列是化合物名称
        for enzyme in df_interaction.columns[1:]:  # 遍历所有酶名称（跳过第一列）
            combinations.append([f"{compound}-{enzyme}", row[enzyme]])

    # 保存到CSV文件
    combinations_df = pd.DataFrame(combinations, columns=["Pair", "Label"])
    # combinations_df.to_csv("all_pairs.csv", index=False)

    # 2. 随机选择 n 个互作组合（值为1），并改为0
    interaction_pairs = []
    for index, row in df_interaction.iterrows():
        compound = row.iloc[0]
        for enzyme in df_interaction.columns[1:]:
            if row[enzyme] == 1:
                interaction_pairs.append((index, enzyme, f"{compound}-{enzyme}"))

    # 随机选择 n 个互作组合
    random_n = 30
    random_selected = random.sample(interaction_pairs, random_n)

    # 记录被修改的组合
    modified_combinations = [pair[2] for pair in random_selected]

    # 生成新的 DataFrame，将选中的 100 个组合改为 0
    df_modified = df_interaction.copy()
    for index, enzyme, _ in random_selected:
        df_modified.at[index, enzyme] = 0

    # 保存修改后的表格
    df_modified.to_csv("../temp_data/modified_interaction.csv", index=False)

    # 3. 输出被修改的 100 个组合名称，并保存为 CSV 文件
    modified_combinations_df = pd.DataFrame(modified_combinations, columns=["LapRLS_test"])
    modified_combinations_df.to_csv("../temp_data/modified_pairs.csv", index=False)

data_split('../data/nr.xlsx')