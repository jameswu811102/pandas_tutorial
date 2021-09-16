"""
使用concatenate → concat() 函式來合併資料

注意！
concat()函式並非專屬DataFrame的專屬功能
→ pd.concat()

參數補充說明：

* join： 呈現合併後的哪些部份資料
  join = "outer"  →  聯集
  join = "inner"  →  交集

* axis： 資料增加的方向(x軸:欄, y軸:列)
  axis = 0  → 資料往y軸方向增加 → 即資料往index方向增加
  axis = 1  → 資料往x軸方向增加 → 即資料往column方向增加

* sort： 資料的排序
  sort = False  →  資料不做排序(不會影響到資料計算結果，只是版面會雜亂)

* keys： 新增資料群組化後的次索引值
  keys = ["df1次索引值", "df2次索引值", "df3次索引值"]
  使用DataFrame.loc["次索引值"]來進行索引
"""

import pandas as pd

df1 = pd.DataFrame({"A": ["A0", "A1", "A2", "A3"],
                    "B": ["B0", "B1", "B2", "B3"],
                    "C": ["C0", "C1", "C2", "C3"],
                    "D": ["D0", "D1", "D2", "D3"]},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({"A": ["A4", "A5", "A6", "A7"],
                    "B": ["B4", "B5", "B6", "B7"],
                    "C": ["C4", "C5", "C6", "C7"],
                    "D": ["D4", "D5", "D6", "D7"]},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({"A": ["A8", "A9", "A10", "A11"],
                    "B": ["B8", "B9", "B10", "B11"],
                    "C": ["C8", "C9", "C10", "C11"],
                    "D": ["D8", "D9", "D10", "D11"]},
                   index=[8, 9, 10, 11])

df4 = pd.DataFrame({"B": ["B2", "B3", "B6", "B7"],
                    'D': ["D2", "D3", "D6", "D7"],
                    'F': ["F2", "F3", "F6", "F7"]},
                   index=[2, 3, 6, 7])

# 將df1, df2, df3 在index軸的方向上做聯集
pd.concat([df1, df2, df3], join="outer", axis=0, sort=False)

# 將df1, df4 在column軸的方向上做聯集
pd.concat([df1, df4], join="outer", axis=1, sort=False)

# 將df1, df4 在column軸的方向上做交集
pd.concat([df1, df4], join="inner", axis=1, sort=False)

# 將df1, df4 在index軸的方向上做交集
pd.concat([df1, df4], join="inner", axis=0, sort=False)

# 將df1, df2, df3 在index軸的方向上做聯集，並且分別新增DF1、DF2、DF3的次索引值
result = pd.concat([df1, df2, df3], join="outer", axis=0, sort=False, keys=["DF1", "DF2", "DF3"])

print(result.loc["DF1"])
