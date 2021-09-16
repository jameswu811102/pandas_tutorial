# 各國飲酒資料數據分析

import pandas as pd

data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\drinks.txt", sep=",")

# 全世界平均消費啤酒(beer)的數量是多少？  啤酒總和 / 國家總數(項數)
data["beer_servings"].sum() / data.shape[0]
'''或  data[beer_servings].mean()  也可以'''

# 每個洲平均消費啤酒(beer)的數量是多少？
data.groupby("continent").beer_servings.mean()

# 每個洲消費葡萄酒(Win) 的最大值、最小值和平均值是多少？
data.groupby("continent").wine_servings.agg(["max", "min", "mean"]).sort_values("max", ascending=False)

# Bonus: 找出消費葡萄酒最高的前五個國家
data[["country", "wine_servings"]].sort_values("wine_servings", ascending=False).head()
