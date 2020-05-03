#定義函式 def  如果沒寫return 預設回傳None
#num1=int(input("請數入數字"))
#num2=int(input("請數入第二個數字"))
# def Plus(n1,n2):
#   tol = n1 + n2
#   return tol

#var=Plus(num1,num2)
#print(var)
#參數的名稱對應  -->可以直接指定各參數的值
# def Plus(n1,n2):
#   tol = n1 + n2
#   return tol
# var = Plus(n1=1,n2=5)
# print(var)
#接收不定參數 * -->不要事先定義好要幾個參數 將傳入的參數變成tuple處理
# def Student(*name):
#   for i in name:
#     print(i)

# Student("a","b",256)

#計算平均值
def CountAvg(*nums):
  sum=0
  lengh=len(nums)
  for i in nums:
    sum+=i
  return sum/lengh

var=CountAvg(1,9,2)
print(var)