# matplotlib.pyplot(pandas.DataFrame.plot)

"""
重點參數：

data = Series或DataFrame物件
→  要製成圖表的資料數據來源

x = "數據來源的列名或位置"
→  繪製用的數據來源列名或列的位置

y = "數據來源的欄位名或位置"
→  繪製用的數據來源欄位名稱或欄的位置


kind  →  資料數據要製作成何種統計圖表 (常用如下)
kind  =  "line"  →  折線圖
         "bar"   →  垂直長條圖
         "barh"  →  水平長條圖
         "pie"   →  圓餅圖

figsize = (width, length)
→  繪製的圖表大小 (單位為英吋)

title = "圖表名稱"
→  圖表名稱

須注意！ 圖像要顯現最後一行務必加上matplotlib.pyplot.show() (可簡化模組plt.show())

"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\titanic_passengers_list.txt", sep=",")


# 請將欄位名稱Sex改成Gender (請使用replace)
data.columns = data.columns.str.replace("Sex", "Gender")

# 請計算出鐵達尼號乘客的男女數量
male_count = data[data["Gender"] == "male"].Gender.count()
female_count = data[data["Gender"] == "female"].Gender.count()

# 請繪製出表示乘客男女數量的圓餅圖
df_count = pd.DataFrame({"Count": [male_count, female_count]}, index=["male", "female"])
count_chart = df_count.plot(y="Count", kind="pie", figsize=(5, 5), title="People Count Proportion")
plt.show()

"""進階：
labels = ["male", "female"]
values = [male_count, female_count]
colors = ["b", "r"]
plt.pie(values, labels=labels, colors=colors)
plt.title("Peoplo Count Proportion", loc="center")
plt.legend()
plt.show()
"""

# 繪製出鐵達尼號倖存者男女數量的圓餅圖 (倖存者的Survived欄位顯示為1)
male_survivor = data[(data["Survied"] == 1) & (data["Gender"] == "male")].Survived.count()
female_survivor = data[(data["Survived"] == 1) & (data["Gender"] == "female")].Survived.count()
df_survivor = pd.DataFrame({"Survived": [male_survivor, female_survivor]}, index=["male", "female"])
survivor_chart = df_survivor.plot(y="Survived", kind="pie", figsize=(5, 5), title="People Survived Proportion")
plt.show()

"""進階：
labels = ["male", "female"]
values = [male_survivor, female_survivor]
colors = ["b", "r"]
plt.pie(values, labels=labels, colors=colors)
plt.title("People survived Proportion", loc="center")
plt.legend()
plt.show()
"""
