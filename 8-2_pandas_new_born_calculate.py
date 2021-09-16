# 美國嬰兒姓名統計資料

import pandas as pd

data = pd.read_csv(r"‪C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\US_Baby_Names_Lite.txt", sep=",")


# 請找出名字是Emma的所有資料
data[data["Name"] == "Emma"]

# 請找出名字是An開頭，並且是女性的資料 (請分別建立兩個名稱為mask1、mask2的篩選條件)
mask1 = data["Name"].str.startswith("An")
mask2 = data["Gender"] == "F"
data[mask1 & mask2]

# 在2004年，最多美國女生取的「菜市場」名為何
data[(data["Year"] == 2004) & (data["Gender"] == "F")].groupby("Name").Count.sum().sort_values(ascending=False).head(1)
