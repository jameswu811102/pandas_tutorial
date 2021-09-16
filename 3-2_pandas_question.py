# Series能否使用中括弧取得區間資料？ (即能否使用iloc[] & loc[] ？)

# 請試著取出球隊欄位(Team)，索引值3到6的資料(不包含索引值7的元素)

import pandas as pd

data = pd.read_csv(r"C:\Users\Wu Cheng Yu\Desktop\Python 總夾\Python 資料分析 - 入門實戰\Euro_2012_stats_TEAM.txt", sep=",")
print(data)


sepTeam = data.Team.iloc[3:7]
# or data.Team[3,7]
print(sepTeam)
