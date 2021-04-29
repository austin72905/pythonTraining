formDataStr="""
--------------------------284d1eea235f7379
Content-Disposition: form-data; name="merchant_id"

JM188098
--------------------------284d1eea235f7379
Content-Disposition: form-data; name="order_sn"

TX20210428154531116
--------------------------284d1eea235f7379
Content-Disposition: form-data; name="daifu_sn"

DFW20210428154535209uk
--------------------------284d1eea235f7379
Content-Disposition: form-data; name="amount"

100.00
--------------------------284d1eea235f7379
Content-Disposition: form-data; name="result"

finish
--------------------------284d1eea235f7379
Content-Disposition: form-data; name="sign"

7245075c17ed05c81e9a1f440fea4cba
--------------------------284d1eea235f7379--
"""

formDataStr = formDataStr.replace("\n","")
# form-data 分割的字串
dataList = formDataStr.split("284d1eea235f7379")
#print(dataList)
for i in dataList:
    
    if(i != "--------------------------"):
        i = i.replace("--------------------------","").replace("Content-Disposition: form-data; name=","")
        keyVal = i.split("\"")
        if keyVal[0] !="--":
            print(keyVal[1]+":"+keyVal[2])