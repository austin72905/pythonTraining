List_l1 = list(input("請輸入第一個字串"))
List_l2 = list(input("請輸入第二個字串"))
List_l3 = list(input("/diff/concat/anys?"))

Str_s1 = "".join(List_l1) 
Str_s2 = "".join(List_l2)
Str_s3 = "".join(List_l3)
print("----------------結果-----------------") 
print("第一個字串長度: ",len(Str_s1)) 
print("第二個字串長度: ",len(Str_s2)) 
if("%2"in Str_s1 or "%2"in Str_s2): 
    print("有被urlencode")


  #轉換成符合postman的格式
if(Str_s2 == "done"): 
    Str_ChgFitPost = Str_s1.replace("=",":").replace("&","\n") 
    print(Str_ChgFitPost)
  #unicode轉中文
elif(Str_s2 == "decode"):
    print(Str_s1.encode('latin-1').decode('unicode_escape'))

elif(Str_s1 == Str_s2): 
    print("兩者相同")

elif(Str_s1 != Str_s2): 
    print("兩者不同")



#如果最後輸入diff，就會顯示差異部分、concat可拼接字串
if(Str_s3 == "diff"):

    print("***************差異部分*****************") 
    Int_Distance = len(List_l1)-len(List_l2)
    Bool_longer = len(List_l1)>len(List_l2)
    Range_lgOne = range(len(List_l1) if Bool_longer else len(List_l2)) 
    i=0

    for i in Range_lgOne: 
        #不足的部分用空字串補起來
        if(Int_Distance >0 ): 
            List_l2.extend(" "*Int_Distance)

        elif(Int_Distance < 0): 
            #絕對值
            List_l1.extend(" "*abs(Int_Distance)) 
        
        if(List_l1[i] != List_l2[i]): 
            print("char in postion "+str(i)+" is different,diff char: "+List_l1[i] +" --- "+List_l2[i])
elif(Str_s3=="concat"):
    #拼接RSA私鑰、平台公鑰
    Str_skey = Str_s1.replace("\n\r"," ").replace(" ","")
    Str_pkey = Str_s2.replace("\n\r"," ").replace(" ","")
    print("-----拼接字串結果-----")
    print(Str_skey+","+Str_pkey)

elif(Str_s3 == "anys"):
    #分析字串長度 接起來密鑰的長度(md5,rsa公,rsa私)
    Ans_Str_List = Str_s1.split(',')
    Ans_Str_List2 = Str_s2.split(',')
    

    
    print("-----------字串一---------------")
    #print("key1: "+len_list[0]+"\n"+"key2: "+len_list[1]+"\n"+"key3: "+len_list[2])
    print("key1: "+str(len(Ans_Str_List[0]))+"\n"+"key2: "+str(len(Ans_Str_List[1]))+"\n"+"key3: "+str(len(Ans_Str_List[2])))
    print("-----------字串二---------------")
    #print("key1: "+len_list2[0]+"\n"+"key2: "+len_list2[1]+"\n"+"key3: "+len_list2[2])
    print("key1: "+str(len(Ans_Str_List2[0]))+"\n"+"key2: "+str(len(Ans_Str_List2[1]))+"\n"+"key3: "+str(len(Ans_Str_List2[2])))


# text ="\u4f60\u662f\u767d\u7661"
# text1=text.encode()#.decode('utf-8')
# print(text1)

