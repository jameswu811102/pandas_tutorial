# 簡訊內容處理字串方法
"""
pandas.Series.str.處理字串函式名稱()

pandas常見字串函式：
upper(arg)    →   字母全改大寫
lower(arg)    →   字母全改小寫
len(arg)      →   計算字串整體長度(字數計算)
title(arg)    →   字串內單字首字母大寫
replace(*arg) →   "被取代單字", "取代單字"
split(arg)    →   以符號切割字串

進階：
startswith(arg)  →  尋找字串包含符號或字母"arg"開頭的字
endswith(arg)    →  尋找字串包含符號或字母"arg"結尾的字
contains(arg)    →  尋找字串包含符號或字母"arg"的字


注意！
須注意資料的類型是否為pandas.Series物件
若為python本身字串物件，則需使用python內建字串函式

"""

import pandas as pd

data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\message.txt", sep="\t", names=["status", "msg"])


# 請將data中，status欄位的字母全改為大寫
data["status"].str.upper()

# 請將data中，status欄位的字母全改為小寫
data["status"].str.lower()

# 請將data中，status欄位的字母開頭改為大寫
data["status"].str.title()

# 請將data中，status欄位的ham字串置換成not spam
data["status"].str.replace("ham", "not spam")

# 請將data中，msg欄位內容以逗號做切開
data["msg"].str.split(",")

# 請尋找data中，msg欄位內容中含a開頭單字的資料有哪些
data[data["msg"].str.startswith("a")]

# 請過濾出不是垃圾信件的e-mail有哪些 (並建立一個mask1物件用作篩選非垃圾信)
mask1 = data["status"] == "ham"
data[mask1]

# 請過濾出不是垃圾信件外，還包含英文單字OK的資料有哪些 (並建立一個mask2物件用作篩含OK單字的資訊)
mask2 = data["msg"].str.contains("OK")
data[mask1 & mask2]

# 請將欄位名稱變成全部大寫()
data.columns = data.columns.str.upper()

# 請建立一個「英文單字開頭是L」的過濾條件mask3，並與前面的mask1及mask2用and合併 (注意欄位名稱已改變)
mask3 = data["MSG"].str.startswith("L")
data[mask1 & mask2 & mask3]
