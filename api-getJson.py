import urllib.request as req
import json # load --> 字串轉list、dic    dump -->物件轉str   indent => 可以使得數據存儲的格式容易解讀。 intent=行數

src="https://datacenter.taichung.gov.tw/swagger/OpenData/8a67f279-a41b-49b3-abb9-2495e1a87751"
with req.urlopen(src) as res: # res 是一個http物件
  
  data=json.load(res) #list 

#print(type(data))  ....py可以連物件都印出來
with open("JsonClinic.txt",mode="w",encoding="utf-8")as file:
  for clinic in data:
    if(clinic["鄉鎮市區"]=="北區"):
      file.write(clinic["合約醫療院所名稱"]+"\n")
      #print(clinic["合約醫療院所名稱"])




