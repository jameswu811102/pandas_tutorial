# 就業資料分析 aggregate → agg()

import pandas as pd

data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\pandas practice.txt",
                   sep="|",
                   index_col="user_id")

# 取得每一個職業的年齡平均值
data.groupby("occupation").age.mean()


# 使用函式agg()取得每一個職業的年齡平均值
data.groupby("occupation").age.agg("mean")


# 使用函式agg()取得每一個職業的年齡最小值、最大值、平均值和數量
'''agg(["函式名稱1", "函式名稱2", "函式名稱3"......])'''
data.groupby("occupation").age.agg(["min", "max", "mean", "count"])


# 將欄位名稱和函式名稱放入agg()參數，取得每一個職業的年齡平均值
'''agg({"欄位名稱1":"函式名稱1, "欄位名稱2":"函式名稱2",......})'''
data.groupby("occupation").agg({"age": "mean"})


# 將欄位名稱和函式名稱放入agg()參數，取得每一個職業的年齡平均值及每一個性別的數量
data.groupby(["occupation", "gender"]).agg({"age": "mean", "gender": "count"})
