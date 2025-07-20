import pandas as pd


def data_todic(PATH, SHEET):
    # 读取 Excel 文件
    file_path = PATH  # 替换为实际的文件路径
    sheet_name = SHEET    # 替换为实际的 sheet 名称

    # 读取 Excel 文件的指定 sheet
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

    # 将数据转换为字典
    result = {}
    data_m = df.iloc[0, 1:].tolist()  # 获取名称列表

    for i in range(1, len(df)):
        current_data = df.iloc[i, 0]
        scores = df.iloc[i, 1:].tolist()
        for j, score in enumerate(scores):
            key = f"{current_data}-{data_m[j]}"
            result[key] = score

    # pd.DataFrame.from_dict(result, orient='index', columns=['value']).to_excel("output/LapRLS_train.xlsx", index=True)  # 字典写入excel

    return result
