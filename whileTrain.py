#range() 幫你生成一個連續數列
# n=1
# while n<5:
#   if n==3 :
#     break
#   n+=1
# print(n)
#for、continue  -->跳過那回
#迴圈裡的else -->在迴圈結束前會執行裡面的東西
# n=0
# for i in range(5):
#   if i%2==0:
#     continue
#   n+=1
# else:
#   print(n)
# 找出輸入的數字，的平方根，若無法整除，打印出"沒有整數的平方根"
num=int(input("請輸入數字"))
for i in range(num):
  if i*i==num:
    print("其平方根為:",i)
    break
else:   
  print("沒有整數平方根")

