# Youtube 頻道排行資料清洗 & 整理示例

"""
重要功能：

pandas.DataFrame.info()
→  確認資料的資訊及資料型態

pandas.Series.str.replace()
→  取代某個字串或符號  --  進階：用來移除符號使字串內容連貫

pandas.Series.astype("欲轉換的資料類型")
→  轉換欄位的資料型態

pandas.DataFrame.drop(labels= , axis= , inplace= )
→  刪除欄位
                      labels  = 要進行刪減的標籤(index or column)為何
                      aixs    = 從欄(axis=1)或列(axis=0)的方向進行資料刪減
                      inplace = 直接取代原資料(True)或不予取代(False)
官方API文件：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html

pandas.Series.unique()
→  尋找欄位中有哪些不重複的值

pandas.Series.map("用做資料傳換的字典")
→  對欄位中的值，對照轉換字典後，予以轉換

"""

import pandas as pd

data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\youtube-channels-data-from-socialblade.txt", sep=",")

# 請先確認分析資料的資訊及資料型態
data.info()

# 請將分析資料中，Rank欄位的資料型態轉為int64
data["Rank"] = data["Rank"].str[0:-2].str.replace(",", "").astype("int64")

"""也可用函式或是生成式的方式處理"""
"""
函式：
def rank_fix(a): 
    
    a = int(a[:-2].replace(",", ""))
    
    return a

data.Rank = data.Rank.apply(rank_fix)
"""
"""
生成式：
data.Rank = [int(x[0:-2].replace(",", "")) for x in data["Rank"]]
"""


# 請將分析資料中，Subscribers欄位的資料型態轉為int64
data["Subscribers"].astype("int64")
invalid_data = data[data["Subscribers"].str.contains("--")].index
data.drop(labels=invalid_data, axis=0, inplace=True)
data["Subscribers"] = data["Subscribers"].astype("int64")

# 尋找Grade欄位中有幾種等級分類 (印出的結果不可包含多餘空白)
"""提示：strip()"""
data["Grade"] = data["Grade"].str.strip(" ")
data["Grade"].unique()

# 請將Grade欄位的資料，依照提供之分數對照表之內容，轉換為實際獲取分數
# (須注意是否有每個都有對應過去  →  最後檢查是否有空值，有的話請刪除)
grade_trans = {"A++": 5, "A+": 4, "A": 3, "A-": 2, "B+": 1}
data["Grade"] = data["Grade"].map(grade_trans)
data.dropna(axis=0, how="any")

# 最後由於資料有刪減的動作，請重新設定索引值使索引值跟資料總比數相符
data.reset_index(drop=True, inplace=True)
"""或是 data.index = range(1, len(data)+1)"""
