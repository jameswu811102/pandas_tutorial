import pandas as pd
import numpy as np


data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\wine.txt", sep=",")


# 請移除掉第0,3,6,8,11,12,13欄位
drop_columns = data.columns[[0, 3, 6, 8, 11, 12, 13]]
data.drop(labels=drop_columns, axis="columns", inplace=True)


# 請重新建立欄位名稱如下
new_columns = ["alcohol", "hue", "alcalinity_of_ash", "magnesium", "flavanoids", "proanthocyanins", "malic_acid"]
data.columns = new_columns


# 設定空值
"""
請將第一欄alcohol，索引值1和2的資料改為空值
請將第二欄hue，索引值3和4的資料改為空值
"""
data["alcohol"].iloc[1:3] = np.nan
data["hue"].iloc[3:5] = np.nan


# 請將欄位alcohol欄位的空值轉為0
data["alcohol"].fillna(0, axis="index", inplace=True)


# 請將DataFrame中剩餘的空值刪除
data.dropna(axis="index", how="any", inplace=True)


# 請將整份資料文件的索引值index重置
data.reset_index(drop=True, inplace=True)

"or data.index = range(1, len(data)+1)"
