#安全關閉檔案的語法  可以不用close釋放資源
#with open(檔案路徑,mode=開啟模式) as  檔案obj:

#儲存檔案
# file=open("demo.txt",mode="w",encoding="utf-8") #創建並寫入檔案，重新打開在寫入會覆蓋
# file.write("中文要加utf-8\nopen again") #寫的內容
# file.close  #關閉，釋放資源
#實務最佳寫法
# with open("demo.txt",mode="w",encoding="utf-8") as file :
#     file.write("這種寫法不用close\n你知道嗎")

#讀取檔案
# with open("demo.txt",mode="r",encoding="utf-8") as file :
#     read=file.read()
# print(read)
# 一行一行讀取
# with open("demo.txt",mode="w",encoding="utf-8") as file :
#      file.write("1\n9")
# sum=0
# with open("demo.txt",mode="r",encoding="utf-8") as file :
     
#      for line in file:
#         sum+=int(line)
            
# print(sum)

#算文件總字元數
# with open("demo.txt",mode="r",encoding="utf-8") as file :
#     read=file.read()
#     lengh=len(read)
# print(lengh)

#使用json格是讀取、複寫檔案
import json
with open("config.json",mode="r") as file:
    data=json.load(file)  #json裡的load方法
print("name:",data["name"]) #json本身是dic
print("version:",data["version"])
# 寫入json
data["name"]="new austin"
with open("config.json",mode="w") as file:
    json.dump(data,file) #把新寫的資料覆寫回檔案中 dump(要寫入的資料,檔案obj)
 
