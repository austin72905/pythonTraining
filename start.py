# 第一隻python
# 有順序、可動的列表 List
[3,4,5]
["hi","hello"]
#有順序、不可動的列表 tuple
(3,5)
("你好","hi")
# 集合 set
{3,4,5}
{"coco","nana"}
#字典 dictionary
{"月月":"austin","句句":"mimi"}
# 數字運算 +-*/、//整數除法0.6->0(只看整數)、**次方、%餘數
#x=2//3
#字串串接 \ -->跳脫字元  \n -->換行 (""")  *乘法可重複
a="hello\n"*3
# 字串會對內部的字元編號(索引) 字串[索引]
b= "austin" #b[0:5] austi、 b[3:] tin
# 有序、可變動的List  grade[0:3]=[] -->可以內索引0~3元素清空 、grade+=["aa","bb"] -->可用加的新增元素、長度len
grade=[1,3,5,1,9]
# 巢狀list  data[0][0:2]=[101,1,1]-->可直接指定換掉資料
data=[[1,2,3],[1,5,9]]
# tuple -->跟list操作一樣，但不可變動資料
#集合 set1={1,2,3}   in  not、in -->布林值、
set1={1,2,3}
set2={3,5,6,7}
#s3=set1&set2  #& 交集  if 都沒交集 set()、
#s3=set1|set2  #| 聯集  取兩個集合的所有資料，重複地只取一次
#s3=set1-set2  #- 差集  減去重疊的部分
#s3=set1^set2   #^反交集  取兩個集合不重複的部分
#把字串拆解成集合  無順序
s=set("austin")
#字典的運算
dic={"月月":"austin","喳喳":"bird"}
# 刪除key  del dic["月月"]
# 從列表資料產生字典
money=[1,2,3]
dic1={x:x**3 for x in money}
print(dic1)