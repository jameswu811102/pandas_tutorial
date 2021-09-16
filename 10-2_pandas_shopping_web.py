# 購物網站國家購買交易資料視覺化

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\online_shopping_retail.txt", sep=",")


# 請取得每個國家的整體消費物品總量為何
consume_per_country = data.groupby("Country").Quantity.sum()


# 將國家的整體消費量做降冪排列，並取得第二名至第十名的國家消費量資料
consume_two_to_ten = consume_per_country.sort_values(ascending=False).iloc[1:10]


# 請將第二名至第十名的國家消費量資料繪製成長條圖
consume_two_to_ten.plot(y="Country", kind="bar", figsize=(10,5), title="Consume 2nd-10th")
plt.show()
