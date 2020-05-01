import random
import statistics as stat

#隨機選取 choice、sample
#data=random.choice([1,3,5,7])
#data=random.sample([1,3,5,7],3)

#隨機調換順序 shuffle
# data=[1,3,5,7]
# random.shuffle(data)

#取得隨機亂數
#data=random.random()  # 0~1 隨機
#data=random.uniform(0.0,1.0) #0.0~1.0 隨機

#取得常態分配亂數
#data=random.normalvariate(100,10)  #normalvariate(平均數,標準差)

#統計模組
#data=stat.mean([1,3,5,7]) #平均數
#data=stat.median([1,3,5,7,100,12,50]) #中位數，會忽略極端值
data=stat.stdev([1,3,5,7,21,12,30]) #標準差:資料的分布狀況
print(data)