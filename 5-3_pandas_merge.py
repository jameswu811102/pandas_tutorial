# 基於特定欄位的資料合併 merge()
"""
pd.DateFrame.merge()

參數補充說明：

* on： 資料要依據哪一個欄位來做合併
  on = "合併資料的依據欄位"
  left_on   = "原資料指定欄位"
  right_on  = "被併資料指定欄位"
  → 若沒指定，系統會自動抓取內容值相同的欄位，若多個欄位，這多個欄位內的值要相同

* how： 資料合併後如何呈現
  how = "left"   →  原合併資料 + 交集部份
  how = "right"  →  被合併資料 + 交集部份
  how = "outer"  →  取資料的交集
  how = "inner"  →  取資料的聯集

* indicator： 顯示資料合併後位於哪個區塊
  → 會自動新增欄位 _merge ，其中的值為(left_only、right_only、both)
  indicator = True

* suffixes： 指定欄位合併後，對其餘有相同值的欄位增加後綴詞
  suffixes = ["原資料同值欄位增加的後綴詞", "被併資料同值欄位增加的後綴詞"]


"""

import pandas as pd

L1 = pd.DataFrame({"Keys": ["K0", "K1", "K2", "K3"],
                   "A": ["A0", "A1", "A2", "A3"],
                   "B": ["B0", "B1", "B2", "B3"]},
                  index=[0, 1, 2, 3])

R1 = pd.DataFrame({"Keys": ["K0", "K1", "K2", "K3"],
                   "C": ["C0", "C1", "C2", "C3"],
                   "D": ["D0", "D1", "D2", "D3"]},
                  index=[0, 1, 2, 3])

L2 = pd.DataFrame({"Key1": ["K0", "K0", "K1", "K2"],
                   "Key2": ["K0", "K1", "K0", "K1"],
                   "A": ["A0", "A1", "A2", "A3"],
                   "B": ["B0", "B1", "B2", "B3"]},
                  index=[0, 1, 2, 3])

R2 = pd.DataFrame({"Key1": ["K0", "K1", "K1", "K2"],
                   "Key2": ["K0", "K0", "K0", "K0"],
                   "C": ["C0", "C1", "C2", "C3"],
                   "D": ["D0", "D1", "D2", "D3"]},
                  index=[0, 1, 2, 3])

# 將L1、R1使用merge()做資料合併
L1.merge(R1, on="keys")

# 將L2、R2使用merge()做資料合併
""" 注意因是多個欄位，因此要多個欄位內的值相同才會進行merge() """
L2.merge(R2, on=["Key1", "Key2"])

# 將L2、R2合併後，資料以left join的方式呈現
L2.merge(R2, on=["Key1", "Key2"], how="left")

# 將L2、R2合併後，資料以right join的方式呈現
L2.merge(R2, on=["Key1", "Key2"], how="right")

# 將L2、R2合併後，資料以outer join的方式呈現
L2.merge(R2, on=["Key1", "Key2"], how="outer")

# 將L2、R2合併後，資料以inner join的方式呈現
L2.merge(R2, on=["Key1", "Key2"], how="inner")

# 將L2、R2以outer join合併後，加入indicator參數，觀察資料的所在區塊為何
L2.merge(R2, on=["Key1", "Key2"], how="outer", indicator=True)

# 指定欄位合併後，利用suffixes對其餘有相同值的欄位增加後綴詞，避免混淆
L2.merge(R2, on="Key1", how="outer", suffixes=["_L", "_R"], indicator=True)
