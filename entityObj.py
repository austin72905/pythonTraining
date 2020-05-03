#建立實體物件、屬性 __init__(self) (與類別的屬性不同)
# 第一種表示法
# class Point:
#   def __init__(self):
#     self.x=3
#     self.y=4

#第二種表示法
# class Point:
#   def __init__(self,x,y):
#     self.x=x
#     self.y=y

# point1=Point(3,4)
# point2=Point(5,5)
# print(point1.x,point1.y)
# print(point2.x,point2.y)

#呼叫實體method
# class Point:
#   def __init__(self,x,y):
#     self.x=x
#     self.y=y
#   #定義實體方法
#   def Show(self):
#     print(self.x,self.y)

# #把物件實體化出來
# point1=Point(3,4)
# #呼叫方法
# point1.Show()

#運用實體包裝讀取檔案的方法
class File():
  def __init__(self,name):
    self.name=name
    self.act=None
  def OpenAndRd(self):
    self.act=open(self.name,mode="r",encoding="utf-8") #OBJ <class '_io.TextIOWrapper'>
    #print(type(self.act))
    return self.act.read() #回傳的是一個字串
    self.act.close()
  def Write(self,content):
    self.act=open(self.name,mode="w",encoding="utf-8")
    self.act.write(content)
    self.act.close()
  
#實體化物件
file1=File("data.txt")
file1.Write("123456")
StringData=file1.OpenAndRd()  #字串

print(StringData)

#實體化物件
file2=File("data2.txt")
file2.Write("我有大老二")
StringData2=file2.OpenAndRd()

print(StringData2)