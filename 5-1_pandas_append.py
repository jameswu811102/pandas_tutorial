"""
使用append()來合併兩個DataFrame資料

pd.DataFrame.append([df1, df2, df3, ......])

* append()中的參數:
  ignore_index = boolean
"""
"""
新增一筆資料方式

* loc[索引值] = [資料1, 資料2,......]  
→ 須知道最後一筆資料的索引值 

* append({"欄位1":"資料1", "欄位2":"資料2",......})  
→ 穩妥，但最後務必加上 ignore_index = True 的參數
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

# 將df1、df2使用append()合併
df1.append(df2)

# 將df1、df2、df3資料使用append()合併
df3 = pd.DataFrame({"A": ["A8", "A9", "A10", "A11"],
                    "B": ["B8", "B9", "B10", "B11"],
                    "C": ["C8", "C9", "C10", "C11"],
                    "D": ["D8", "D9", "D10", "D11"]},
                   index=[8, 9, 10, 11])

df1.append([df2, df3])

# 合併df1、df4，並使用參數ignore_index來建立新的index

df4 = pd.DataFrame({"B": ["B1", "B2", "B3", "B4"],
                    "D": ["D1", "D2", "D3", "D4"],
                    "E": ["E1", "E2", "E3", "E4"]},
                   index=[2, 3, 4, 5])

df1.append(df4, ignore_index=True)

# 在df4中，新增 B5、D5、E5 (用loc方式) 及B6、D6、E6 (用append方式)等六筆資料
df4.loc["6"] = ["B5", "D5", "E5"]

df4 = df4.append({"B": "B6", "D": "D6", "E": "E6"}, ignore_index=True)
