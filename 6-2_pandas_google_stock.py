"""
pandas_datareader套件 (抓取yahoo股價資訊)

* get_data_yahoo("上市股票名稱", 抓取起訖時間, 抓取終止時間)
  時間需使用datetime時間物件

  DataReader("上市股票名稱", "抓取的來源搜尋引擎", 抓取起訖時間, 抓取終止時間)

* pandas的DatetimeIndex概念：
  index既是索引值，也是Datetime時間物件
  → 用index來做操作等同用Datetime時間物件再做操作

* resample("新計算週期或頻率")
  分鐘 → T
  天數 → D

"""

import datetime as dt
import pandas_datareader as pdr

# 請抓取google股價資訊 (間隔；2020-03-01 ~ 2020-04-30)
"google上市名稱：GOOG"

start = dt.datetime(year=2020, month=3, day=1)
end = dt.datetime(year=2020, month=4, day=30)
stock = pdr.get_data_yahoo("GOOG", start, end)

"""
或也可寫作stock = pdr.DataReader("GOOG", "yahoo", start, end) 
"""


# 請計算每周交易量
"""
1. 先求各筆資料對應週數 (DatetimeIndex概念)
2. 將對應週數新增一欄到原資料中
3. 運用分組概念求解
"""
weeks = stock.index.isocalendar().week
stock["weeks"] = weeks
stock.groupby("weeks").Volume.sum()


# 將抓取的週期(頻率)由「每天」改為「十天」，並計算十日均線
"十日均線： 十天結算一次的平均資料"
stock_per_10day = stock.resample("10D").mean()
