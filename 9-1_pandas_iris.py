# 鳶尾花資料清洗 & 整理示例

"""
重要功能：

del DataFrame("欄位名稱")
→  刪除欄位

pandas.DataFrame.isnull()
→  檢查是否有空值Null  (回傳布林物件)

pandas.DataFrame.isnull().sum()
→  用以檢查空值共有幾個

pandas.DataFrame.iloc[範圍] = numpy.nan
→  建立空值

pandas.DataFrame.dropna(axis= , how= , inplace= )
→  刪除空值
                        axis=0     →  出現空值的目標列予以刪除
                        axis=1     →  出現空值的目標欄予以刪除
                        how="any"  →  只要目標列或目標欄有空值即將空值移除
                        how="all"  →  必須整列或整欄皆為空值才將空值移除
                        inplace    →  是否直接取代原表格資料(True or False)
　
pandas.DataFrame.fillna(value="空值欲填入內容", inplace=True or False)
→  空值填入內容，是看是否直接取代原資料

pandas.DataFrame.reset_index(drop=True, inplace= True or False)
→  重置索引值
                        drop=True  →  將原本索引值欄位刪除，避免產生新舊索引欄並存之情形
                        inplace=   →  是否直接取代原資料
"""


import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\Iris.txt", sep=",", names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])

# 分析資料時，因不會使用到class欄位，請使用del語句刪除該欄位
del data["class"]


# 請確認分析資料中，是否有空值(Null)
data.isnull().sum()

"""或也可以使用data.info()的方式來知曉"""


# 請在sepal_width欄位，index=1 至 index=3之間建立空值
data["sepal_width"].iloc[1:4] = np.nan


# 請將上述建立在sepal_width的空值替換為0
data.fillna(0, inplace=True)


# 請在sepal_length欄位，index=1 至 index=3之間建立空值
data["sepal_length"].iloc[1:4] = np.nan


# 請將上述建立在sepal_length的空值予以刪除
data.dropna(axis=0, how="any", inplace=True)


# 最後請將整份分析資料的索引值予以重置
data.reset_index(drop=True, inplace=True)
