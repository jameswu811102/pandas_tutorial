# 資料分析用第三方庫: pandas (pd)
# 統計分析用第三方庫: numpy (np)

# 主要集中在pandas的學習，因pandas是在numpy的基礎上發展而來，兼容了numpy的優點


# 基礎numpy功能介紹

import numpy as np

list1 = [2, 4, 6, 8, 10]
array1 = np.array(list1)
print(list1)
print(array1)
print(array1.dtype)

array2 = array1.astype(np.float64)
print(array2.dtype)

print(array1 * 5)
print(array2 * 5)

array3 = array1 + array2
print(array3)

print(" ")
###############################################################
print(" ")

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

array1 = np.array(list1)
array2 = np.array(list2)

print(array1[0])
print(array1[-1])
print(array1[0:5])
print(array1[0:5:2])
print(array1[::-1])

print(array2[0])
print(array2[-1])
print(array2[2:])
print(array2[:4])
print(array2[::-2])

array1[-1] = 99
array2[-1] = 100
print(array1)
print(array2)

print(" ")
###############################################################
print(" ")

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

array1 = np.array(list1)
array2 = np.array(list2)

print(array1)
print(array2)

array1 = array1.reshape((2, 2))   # 將array1轉為2維矩陣
print(array1)
array2 = array2.reshape((2, 2))   # 將array2轉為3維矩陣
print(array2)

array3 = array1.dot(array2)
print(array3)
