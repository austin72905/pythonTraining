import difflib


string1=tuple(input("請輸入第一個字串"))
string2=tuple(input("請輸入第二個字串"))
str1="".join(string1)
str2="".join(string2)

if(str1==str2):
    print("兩者相同")

d=difflib.Differ()
diff=d.compare(str1.splitlines(),str2.splitlines())
print("-------------------------比對結果-----------------------")
print("字串一長度: ",len(string1))
print("字串二長度: ",len(string2))
print("\n".join(list(diff)))
#不一樣的索引值，字串二比字串一多了、少了那些
