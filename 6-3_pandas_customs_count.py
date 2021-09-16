# 餐廳來客數量分析
"""
將index欄位轉換成DatetimeIndex
→ pandas.to_datetime(要轉換的欄位)

"""

import pandas as pd

data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\RestaurantVisitors.txt", sep=",")

# 將date欄位轉為DatetimeIndex
data.index = pd.to_datetime(data["date"])


# 第一間餐廳rest1，每週來客數總和多少？
data["located_week"] = data.index.isocalendar().week
data.groupby("located_week").rest1.sum()


# 計算節日(holiday)四間餐廳平均來客數
"""
1. 使用欄位Holiday找出假日資料
2. 使用iloc過濾四間餐廳的來客數
3. 最後算出平均值
"""
data[data.holiday == 1].iloc[:, 4:8].mean()


# 非假日四間餐廳平均來客數
data[data.holiday == 0].iloc[:, 4:8].mean()


# Bonus：
"""
1. 請算出除了是節日之外，亦包含禮拜六或禮拜天的四間餐廳平均來客數
2. 請算出非節日且不是禮拜六及禮拜天的四間餐廳平均來客數
"""

data[(data.holiday == 1) | (data.weekday == "Saturday") | (data.weekday == "Sunday")].loc[:, "rest1": "rest4"].mean()

data[(data.holiday == 0) & ((data.weekday != "Saturday") & (data.weekday != "Sunday"))].loc[:, "rest1": "rest4"].mean()
