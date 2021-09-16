# 股價圖實作 (line chart & candlestick chart)
"""
matplotlib.pyplot

import matplotlib.pyplot as plt

建立空圖表：
plt.figure(figsize=(寬, 長))

建立資料線圖：
plt.plot(繪圖df資料源, label="線條名稱")

建立圖表標題：
plt.title("圖表名稱", loc="left" or "center" or "right")

建立圖表X軸單位名稱：
plt.xlabel("X軸名稱")

建立圖表Y軸單位名稱：
plt.xlabel("Y軸名稱")

建立網格線：
plt.grid(b=是否開啟網狀格顯示, axis="x" or "y" or "both")

建立圖表圖例：
plt.legend()

呈現繪製好之圖表：
plt.show()

"""
#############################################################
"""
pandas_datareader

import pandas_datareader as pdr

pdr.DataReader("股價代碼", "抓取來源網站名", 起始時間, 結束時間)
須注意抓取台股時，股價代碼需加上 ".tw"
→ 如台積電應寫作 "2330.tw"

"""
#############################################################

"""
mplfinance

import malfinance as mpf

mpf.plot(繪圖用完整df資料源(非欄位), type="圖表種類", mav=移動均線計算天數頻率, volume=交易量呈現與否)

可參Github使用文件：https://github.com/matplotlib/mplfinance
"""


import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt
import mplfinance as mpf


# 取得台積電與聯發科的歷史股價訊息 (時間區間為2020/1/1 - 2020/6/1)
"""台積電(TSMC)      ：Stock Code:2330
   聯發科(MediaTek)  ：Stock Code:2454"""

start = dt.datetime(2020, 1, 1)
end = dt.datetime(2020, 6, 1)
tsmc = pdr.DataReader("2330.tw", "yahoo", start, end)
mediatek = pdr.DataReader("2454", "yahoo", start, end)


# 繪製出TSMC vs MediaTek的線圖
fig = plt.figure(figsize=(10, 5))
plt.plot(tsmc["Close"], label="TSMC")
plt.plot(mediatek["Close"], label="MediaTek")
plt.title(b="TSMC vs MediaTek", loc="center")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True, axis="y")
plt.legend()
plt.show()    # 或fig.show()


# 請繪製出台積電2020/1/1 - 2020/6/12的K線圖，移動均線計算日為10天，並請顯示交易量
mpf.plot(tsmc, type="candle", mav=10, volume=True)
