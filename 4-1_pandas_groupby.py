# 就業資料分析 groupby()、apply()

import pandas as pd
data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\pandas practice.txt",
                   sep="|",
                   index_col="user_id")

# 請計算每個職業的平均年齡
'''提示: groupby()函式'''
avg = data.groupby("occupation").age.mean()


# 分析哪一個職業的男性比例最高
'''
1. 將性別轉換成數字 → 創建一個自定義函式
2. 使用apply()函式 → ()裡面輸入自定義函式的名稱
3. 新增DataFrame欄位 → 新增方式如同字典增加鍵值對的方式
4. 計算比例 → (某職業的男性人數/某職業的總人數)，並做降冪排列就可知道各職業中的男性比例(ascending = False)
'''
# 性別轉換函式


def gender_trans(x):
    if x == "M":
        return 1
    else:
        return 0


# 將gender欄位置換成0、1，並新增到gender_new的欄位中
data["gender_new"] = data["gender"].apply(gender_trans)

# 計算比例(某職業的男性人數/某職業的總人數)，然後再做降冪排列
men_ratio = (data.groupby("occupation").gender_new.sum()) / (data.occupation.value_counts()) * 100

result = men_ratio.sort_values(ascending=False)

print(result)