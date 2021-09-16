import pandas as pd

data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\Euro_2012_stats_TEAM.txt", sep=",")
# data是一個物件(class)，且是一個DataFrame物件

print(data)

# 確認所有欄位的名稱與型態 → 使用DataFrame物件中的dtypes屬性
print(data.dtypes)

# 取得每隻隊伍的黃牌及紅牌數量 → 取資料並形成一個列表[]
cards = data[["Team", "Yellow Cards", "Red Cards"]]
print(cards)

# 哪隊的黃牌數量最多？ → 對黃牌數量進行降冪排列
print(cards.sort_values("Yellow Cards", ascending=False))

# 哪隊的紅牌最多最多？ → 對紅牌數量進行降冪排列
print(cards.sort_values("Red Cards", ascending=False))

# =============================================================
# =============================================================

# Series物件 → 單一行的資料(此以各隊的得分為範例)
print(data.Goals)

# 取得各隊得分的總平均 → mean()功能
print(data.Goals.mean())

# 若要對總平均進行四捨五入 → 使用Python內建的round()功能
print(round(data.Goals.mean()))

# 尋找得分大於平均的隊伍 → 先建立一個篩選器，再進行過濾
score_filter = data.Goals > 5
print(data[score_filter])

# 尋找隊伍名稱是 "S" 開頭的隊伍 → 一樣先篩選器，再過濾
team_filter = data.Team.str.startswith("S")
print(data[team_filter])

# =============================================================
# =============================================================

# 使用index切段的方式來取得資料 → iloc(始列:終列, 始欄:終欄)功能，包頭不包尾
print(data.iloc[0:3, 1:4])

# 使用行列名稱切段的方式來取得資料 → loc("使列名稱":"終列名稱", "始行名稱":"終行名稱")，包頭也包尾
print(data.loc[0:2, "Team":"Hit Woodwork"])
