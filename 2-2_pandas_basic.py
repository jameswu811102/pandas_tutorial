import pandas as pd

data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\pandas practice.txt",
                   sep="|",
                   index_col="user_id")

# sep表示資料的分隔符號為何
# index_col表示資料的索引欄位為何(唯一，如同字典的key)


# 尋找「頭」五筆資料 → head() → 輸入引數表示尋找第幾筆
print(data.head())

# 尋找「尾」五筆資料 → tail() → 輸入引數表示尋找 "倒數" 第幾筆
print(data.tail())

# 資料總列數(幾筆資料) → shape[0]
print(data.shape[0])

# 資料總欄數(幾個大項) → shape[1]
print(data.shape[1])

# 請列出所有欄位的名稱與資料型態 → dtypes
print(data.dtypes)

# 指定欄位 → 檔案.欄位   或   檔案["欄位名稱"][1]
print(data.occupation)
print(data["occupation"])

# 某欄中的第一個值 → 檔案.欄位[1]   或   檔案["欄位名稱"][1]
print(data.occupation[1])
print(data["occupation"][1])

# 某欄中有哪些不重複的值(內容) → unique()
print(data.occupation.unique())

# 某欄中不重複的值有幾項(個數) → nunique()
print(data.occupation.nunique())

# 某欄中不重複的值各自出現的個數計算 → value_counts()
print(data.occupation.value_counts())

# 某欄中哪個不重複的值其出現頻率最高 → head() 參數1表示最高的1項，參數2表示最高的2項...etc
print(data.occupation.value_counts().head(1))

# 某欄中哪個不重複的值其出現頻率最低 → tail() 使用參照head()
print(data.occupation.value_counts().tail(2))

# 獲取表格的基本統計資料 → describe()
print(data.describe())

# 獲取表格的完整基本統計資料 → describe(include = "all")
print(data.describe(include="all"))

# 獲取表格欄位資料型態為object的完整基本統計資料
print(data.describe(include="object"))

# 獲取表格欄位資料型態為integer的完整基本統計資料
print(data.describe(include="integer"))