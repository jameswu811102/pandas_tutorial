# 時間模組使用的重要性：
"""
如:
人事系統中的員工的年假問題
財務報表的週期

注意！
時間的處理是開發人員最常出現錯誤需要debug的地方
"""

"""
python 內建時間模組的應用

* 基本時間表示：
  - class datetime.datetime(args)
    → args：year、month、day、hour、minute、second、microsecond

* 獲取目前時間：
  - class datetime.datetime.today()
  - 獲得單一屬性：datetime時間物件.屬性名稱
    → 物件.year
    → 物件.month
    → 物件.day
    → 物件.hour
    → 物件.minute
    → 物件.second

* 將datetime時間物件透過format轉換成字串(須注意大小寫)
  - datetime時間物件.strftime( "args" )
    → args：%Y、%m、%d、%H、%M、%S (年月日時分秒)
    
* 時間的調整
  - datetime時間物件.timedelta(日期調整幅度)
    → 參數「沒有」年月，且調整參數皆為複數(days、hours、minutes、seconds)
  - 調整方式：
    → 先創建一個「調整幅度物件」
    → 將「原時間物件」與「調整幅度物件」相加
"""

import datetime as dt

# 請製作一個表示 2021/01/01 AM 09:30:30 的時間物件
Date = dt.datetime(year=2021, month=1, day=1, hour=9, minute=30, second=30)


# 獲得目前時間
Today = dt.datetime.today()


# 取得目前時間之物件的各單一屬性
print(Today.year)
print(Today.month)
print(Today.day)
print(Today.hour)
print(Today.minute)
print(Today.second)

# 將目前時間之物件透過format轉換成字串 XXXX-XX-X, XX:XX:XX (format須注意大小寫)
TodayStr = Today.strftime("%Y-%m-%d, %H:%M:%S")


# 將目前時間往前調一年(須注意時間調整沒有年月，且參數為複數)
Delta = dt.timedelta(days=-365)
AdjustTime = Today + Delta

