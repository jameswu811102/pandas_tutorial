# 課後練習 - 墨西哥烤餅Salsa醬的種類與價格分析

import pandas as pd

chipotle = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\chipotle.tsv", sep="\t")


# 獲取欄位的資料型態
chipotle.dtypes


# 將item_price欄位型態從「字串」(object)轉為「浮點數」(float)型態
"""thinking: create a list to append correct item_price data"""

"""最正統方法"""
rm_dollar_sign = []

for price in chipotle.item_price:
    rm_dollar_sign.append(float(price[1:]))

chipotle["item_price"] = rm_dollar_sign


"""快速處理法"""
"""
法1：
chipotle["item_price"] = chipotle["item_price"].str.replace("$", "").astype("float64")

法2：
chipotle["item_price"] = [float(price[1:]) for price in chipotle["item_price"]]

"""


# 計算item_price的平均值(四捨五入到整數)
print(round(chipotle.item_price.mean()))


# 請找出item_price價格大於7的資料
print(chipotle[chipotle.item_price > 7])


# 請找出item_price價格大於7，且choice_description欄位包含Fresh Tomato Salsa的資料
# 提示1: Series.str.contains('比對字串')
# 提示2: 請善用DataFrame[(條件1) & (條件2)]
print(chipotle[(chipotle.item_price > 7) & (chipotle.choice_description.str.contains("Fresh Tomato Salsa"))])


# 請找出item_price最貴的一筆資料(該筆資料含所有的資訊，品名、內容物、價格)
print(chipotle.sort_values("item_price", ascending=False).head(1))


# 請使用iloc切割出第3列到第10列，以及欄位order_id到item_name的資料(注意索引值對應的列數)
print(chipotle.iloc[3:11, 0:3])

# 承上題，換請使用loc切割出第3列到第10列，以及欄位order_id到item_name的資料
print(chipotle.loc[2:9, "order_id":"item_name"])
