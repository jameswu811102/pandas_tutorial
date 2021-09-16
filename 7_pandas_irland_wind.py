# 愛爾蘭地區風速資料分析
"""
1. 正規表示式的使用：
   請參照Python總夾內的講義

2. PeriodIndex物件使用：
   pandas.DatetimeIndex.to_period("頻率參數")
   "M" → 月
   "W" → 週
   "D" → 日
"""

import pandas as pd
import datetime as dt

data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\Ireland_wind.txt", sep="\s+", parse_dates={"year_month_day": [0, 1, 2]}, dayfirst=True)


"""
若只有而沒有parse_dates={"": []}

data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\Ireland_wind.txt", sep="\s+"

則在以下修正年份的地方會出現不同的處理方法
"""


# 將年份錯誤的部份做出修正
"""
1. 觀察錯誤的地方：資料的年份
2. 自行製作一個函式來修正此問題
   → 修正提示：大於2060年的資料減去100，建立新的日期欄位資訊
"""


def fix(arg):                                               # arg會傳入時間物件
    if arg.year > 1978:                                     # 使時間物件得到年分欄位並做判斷
        correct_year = arg.year - 100
    else:
        correct_year = arg.year

    return dt.datetime(correct_year, arg.month, arg.day)    # 條件式判別完後回傳修正後年份，月、日則照舊


data["year_month_day"] = data["year_month_day"].apply(fix)  # 將新的datatimeindex時間物件改寫回去原本欄位


"""
進階寫法：

def fix(arg):
    year = arg.year - 100 if arg.year > 1978 else arg.year
    return dt.datetime(year, arg.month, arg.day)
    
data["year_month_day"] = data["year_month_day"].apply(fix)

"""

"""
導入文件時，沒有加上參數 parse_dates={"": []} 的改寫法：
data.index = ["19{}-{}-{}".format(x, y, z) for x, y, z in zip(data.Yr, data.Mo, data.Dy)]
data.index = pd.to_datetime(data.index)

"""



# 將日期欄位設定為index
data.index = pd.to_datetime(data["year_month_day"])

# 取得每一個地區風速的統計資料，包含平均值、標準差等統計資訊
data.describe()

# 改變統計資料的軸線，取得每一天的風速最小值、最大值、平均值和標準差
data_per_day = pd.DataFrame()
data_per_day["Min"] = data.min(axis=1)
data_per_day["Max"] = data.max(axis=1)
data_per_day["Mean"] = data.mean(axis=1)
data_per_day["StDev"] = data.std(axis=1)
data_per_day

# 取得每個地區一月的平均風速
data.loc[data.index.month == 1].mean()
"""
或簡寫作 data[data.index.month == 1].mean()
"""

# 個地區每一年每個月的平均風速 (提示：PeriodIndex時間物件)
data.groupby(data.index.to_period("M")).mean()

# 個地區每個月的平均風速、最小風速、最大風速
data.groupby(data.index.month).agg(["mean", "min", "max"])

# 個地區每一年每週的平均風速
data.groupby(data.index.to_period("W")).mean()

# 擷取前12筆，從地區RPT到KIL，每一年每月的平均風速、最小風速、最大風速
monthly = data.groupby(data.index.to_period("M")).agg(["mean", "min", "max"])
monthly.loc[monthly.index[0:12], "RPT": "KIL"]
