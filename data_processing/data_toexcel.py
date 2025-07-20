import pandas as pd


def data_toexcel(DATAS, outPATH):
    datas = DATAS
    data = pd.DataFrame(datas)
    writer = pd.ExcelWriter(outPATH)		# 写入Excel文件
    data.to_excel(writer, "Sheet1", float_format='%.5f')		# ‘PAGE’是写入excel的sheet名
    writer.save()
    writer.close()
