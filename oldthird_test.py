# coding: utf-8
oldstr = "ICBC-中国工商银行,ABC-中国农业银行,CCB-中国建设银行,CMB-中国招商银行,PSBC-中国邮政储蓄银行,CIB-兴业银行,CMBC-中国民生银行,BOCO-交通银行,ECITIC-中信银行,CEB-中国光大银行,BOC-中国银行,HXB-华夏银行,PINGAN-平安银行,SPDB-上海浦东发展银行,BCCB-北京银行,BHB-渤海银行,DGB-东莞银行,GZCB-广州银行,HZB-杭州银行,CZB-浙商银行,NJCB-南京银行,NBCB-宁波银行,BJRCB-北京农村商业银行,TJYH-天津银行,HBYH-河北银行,NMGYH-内蒙古银行,EEDSYH-鄂尔多斯银行,DLYH-大连银行,JLYH-吉林银行,HEBYH-哈尔滨银行,JSYH-江苏银行,WZYH-温州银行,SXYH-绍兴银行,SMYH-厦门银行,QZYH-泉州银行,NCYH-南昌银行,QDYH-青岛银行,YTYH-烟台银行,ZZYH-郑州银行,HUBYH-湖北银行,CSYH-长沙银行,CDYH-成都银行,CQYH-重庆银行,GZYH-贵州银行,XAYH-西安银行,LZYH-兰州银行,QHYH-青海银行,NXYH-宁夏银行,HYYH-韩亚银行,ZDYH-中德银行,SMGJYH-厦门国际银行,SDB-深圳发展银行,GDB-广发银行,SHB-上海银行,DGNS-东莞农村商业银行,MYSH-绵阳市商业银行,GDNS-广东农村信用社,CDNS-成都农村商业银行,ZYYH-中原银行,LZYH2-柳州银行,SCNYS-四川省农村信用合作社,JXYH-江西银行,GZNS-贵州农村信用社,SNCCB-遂宁银行,LSCCB-乐山市商业银行,JJBANK-九江银行,KMNX-昆明农村信用社,GSNX-甘肃农村信用社,SHRCB-上海农商银行,GXNXS   -广西壮族自治区农村信用社联合社,GLYH- 桂林银行,FJNXS-福建省农村信用社联合社,AHNXS-安徽省农村信用联社,GYYH-贵阳银行,GSNHJ-甘肃省农村合作金融结算服务中心,HSYH-徽商银行,HBNXS-湖北省农村信用社联合社,JSNXS-江苏省农村信用社联合社,JXNXS-江西省农村信用社联合社,HNNXS-湖南省农村信用社联合社,QHNXS-青海省农村信用社,SJYH-盛京银行,SDNXS-山东省农村信用社联合社,SXNXS-陕西省农村信用社联合社,ZJNXS-浙江省农村信用社联合社,WSYH-网商银行,XJWWENXS-新疆维吾尔自治区农村信用社联合社,NMGNXS-内蒙古农村信用社,TZCB-台州银行,BOSZ-苏州银行,GSBANK-甘肃银行,HENNXS-河南省农村信用社,JLNXS-吉林省农村信用社,YNNXS-云南省农村信用社,GZNSH-广州农村商业银行,HEBNXS-河北省农村信用社联合社,YKYH-营口银行,SZNXS-深圳农村信用社,RZYH-日照银行,JNYH-济宁银行,TJNSYH-天津农商银行,SZNCSYYH-深圳农村商业银行,JNSYYH-济南商业银行,CQSXYH-重庆三峡银行,CQNSYH-重庆农商银行,BSYH-包商银行,CSNCSYYH-常熟农村商业银行,EEDSNSYH-鄂尔多斯农商银行,FDYH-富滇银行,JSHYH-晋商银行,WHNCSYYH-武汉农村商业银行,QLYH-齐鲁银行,CAYH-长安银行,BBWYH-北部湾银行,SXNSYH-陕西农商银行,OTHER-其他银行"


bankDic={"ABC" : "中国农业银行","ARCU": "安徽省农村信用社","ASCB": "鞍山银行","AYCB": "安阳银行","BANKWF": "潍坊银行","BGB" : "广西北部湾银行","BHB" : "河北银行","BJBANK": "北京银行","BJRCB" : "北京农村商业银行","BOC" : "中国银行","BOCD": "承德银行","BOCY": "朝阳银行","BOD" : "东莞银行","BODD": "丹东银行","BOHAIB": "渤海银行","BOJZ": "锦州银行","BOP" : "平顶山银行","BOQH": "青海银行","BOSZ": "苏州银行","BOYK": "营口银行","BOZK": "周口银行","BSB" : "包商银行","BZMD": "驻马店银行","CBBQS" : "城市商业银行资金清算中心","CBKF": "开封市商业银行","CCB" : "中国建设银行","CCQTGB": "重庆三峡银行","CDB" : "国家开发银行","CDCB": "成都银行","CDRCB" : "成都农商银行","CEB" : "中国光大银行","CGNB": "南充市商业银行","CIB" : "兴业银行","CITIC" : "中信银行","CMB" : "招商银行","CMBC": "中国民生银行","COMM": "交通银行","CQBANK": "重庆银行","CRCBANK": "重庆农村商业银行","CSCB": "长沙银行","CSRCB" : "常熟农村商业银行","CZBANK": "浙商银行","CZCB": "浙江稠州商业银行","CZRCB" : "常州农村信用联社","DAQINGB": "龙江银行","DLB" : "大连银行","DRCBCL": "东莞农村商业银行","DYCB": "德阳商业银行","DYCCB" : "东营市商业银行","DZBANK": "德州银行","EGBANK": "恒丰银行","FDB" : "富滇银行","FJHXBC": "福建海峡银行","FJNX": "福建省农村信用社联合社","FSCB": "抚顺银行","FXCB": "阜新银行","GCB" : "广州银行","GDB" : "广东发展银行","GDRCC" : "广东省农村信用社联合社","GLBANK": "桂林银行","GRCB": "广州农商银行","GSRCU" : "甘肃省农村信用","GXRCU" : "广西省农村信用","GYCB": "贵阳市商业银行","GZB" : "赣州银行","GZRCU" : "贵州省农村信用社","H3CB": "内蒙古银行","HANABANK": "韩亚银行","HBC" : "湖北银行","HBHSBANK": "湖北银行黄石分行","HBRCU" : "河北省农村信用社","HBYCBANK": "湖北银行宜昌分行","HDBANK": "邯郸银行","HKB" : "汉口银行","HKBEA" : "东亚银行","HNRCC" : "湖南省农村信用社","HNRCU" : "河南省农村信用","HRXJB" : "华融湘江银行","HSBANK": "徽商银行","HSBK": "衡水银行","HURCB" : "湖北省农村信用社","HXBANK": "华夏银行","HZCB": "杭州银行","HZCCB" : "湖州市商业银行","ICBC": "中国工商银行","JHBANK": "金华银行","JINCHB": "晋城银行JCBANK","JJBANK": "九江银行","JLBANK": "吉林银行","JLRCU" : "吉林农信","JNBANK": "济宁银行","JRCB": "江苏江阴农村商业银行","JSB" : "晋商银行","JSBANK": "江苏银行","JSRCU" : "江苏省农村信用联合社","JXBANK": "嘉兴银行","JXRCU" : "江西省农村信用","JZBANK": "晋中市商业银行","KLB" : "昆仑银行","KORLABANK" : "库尔勒市商业银行","KSRB": "昆山农村商业银行","LANGFB": "廊坊银行","LSBANK": "莱商银行","LSBC": "临商银行","LSCCB" : "乐山市商业银行","LYBANK": "洛阳银行","LYCB": "辽阳市商业银行","LZYH": "兰州银行","MTBANK": "浙江民泰商业银行","NBBANK": "宁波银行","NBYZ": "鄞州银行","NCB" : "南昌银行","NHB" : "南海农村信用联社","NHQS": "农信银清算中心","NJCB": "南京银行","NXBANK": "宁夏银行","NXRCU" : "宁夏黄河农村商业银行","NYBANK": "广东南粤银行","ORBANK": "鄂尔多斯银行","PSBC": "中国邮政储蓄银行","QDCCB" : "青岛银行","QLBANK": "齐鲁银行","SCCB": "三门峡银行","SCRCU" : "四川省农村信用","SDEB": "顺德农商银行","SDRCU" : "山东农信","SHBANK": "上海银行","SHRCB" : "上海农村商业银行","SJBANK": "盛京银行","SPABANK": "平安银行","SPDB": "上海浦东发展银行","SRBANK": "上饶银行","SRCB": "深圳农村商业银行","SXCB": "绍兴银行","SXRCCU": "陕西信合","SZSBK" : "石嘴山银行","TACCB" : "泰安市商业银行","TCCB": "天津银行","TCRCB" : "江苏太仓农村商业银行","TRCB": "天津农商银行","TZCB": "台州银行","URMQCCB": "乌鲁木齐市商业银行","WHCCB" : "威海市商业银行","WHRCB" : "武汉农村商业银行","WJRCB" : "吴江农商银行","WRCB": "无锡农村商业银行","WZCB": "温州银行","XABANK": "西安银行","XCYH": "许昌银行","XJRCU" : "新疆农村信用社","XLBANK": "中山小榄村镇银行","XMBANK": "厦门银行","XTB" : "邢台银行","XXBANK": "新乡银行","XYBANK": "信阳银行","YBCCB" : "宜宾市商业银行","YDRCB" : "尧都农商行","YNRCC" : "云南省农村信用社","YQCCB" : "阳泉银行","YXCCB" : "玉溪市商业银行","ZBCB": "齐商银行","ZGCCB" : "自贡市商业银行","ZJKCCB": "张家口市商业银行","ZJNX": "浙江省农村信用社联合社","ZJTLCB": "浙江泰隆商业银行","ZRCBANK": "张家港农村商业银行","ZYCBANK": "遵义市商业银行","ZZBANK": "郑州银行"}

bankList= [["BOC", "中国银行"],["ICBC", "中国工商银行"],["ABC", "中国农业银行"],["CCB", "中国建设银行"],["CITIC", "中信银行"],["CMB", "招商银行"],["PSBC", "中国邮政储蓄银行"],["CIB", "兴业银行"],["SPDB", "上海浦东发展银行"],["SPABANK", "平安银行"],["CMBC", "中国民生银行"],["COMM", "交通银行"],["GDB", "广东发展银行"],["CEB", "中国光大银行"],["HXBANK", "华夏银行"],["CZBANK", "浙商银行"],["BOD", "东莞银行"],["SXCB", "绍兴银行"],["BOZK", "周口银行"],["BOJZ", "锦州银行"],["BOP", "平顶山银行"],["HKB", "汉口银行"],["BOSZ", "苏州银行"],["HZCB", "杭州银行"],["HSBK", "衡水银行"],["HDBANK", "邯郸银行"],["BJBANK", "北京银行"],["BOCY", "朝阳银行"],["LANGFB", "廊坊银行"],["JNBANK", "济宁银行"],["JINCHB", "晋城银行"],["HBC", "湖北银行"],["BODD", "丹东银行"],["AYCB", "安阳银行"],["EGBANK", "恒丰银行"],["NJCB", "南京银行"],["FDB", "富滇银行"],["KLB", "昆仑银行"],["LSBANK", "莱商银行"],["FXCB", "阜新银行"],["TZCB", "台州银行"],["XCYH", "许昌银行"],["NXBANK", "宁夏银行"],["HSBANK", "徽商银行"],["JJBANK", "九江银行"],["ASCB", "鞍山银行"],["DLB", "大连银行"],["GCB", "广州银行"],["NBBANK", "宁波银行"],["BOYK", "营口银行"],["SXRCCU", "陕西信合"],["GLBANK", "桂林银行"],["BOQH", "青海银行"],["QDCCB", "青岛银行"],["HKBEA", "东亚银行"],["WZCB", "温州银行"],["QLBANK", "齐鲁银行"],["GZB", "赣州银行"],["CQBANK", "重庆银行"],["DAQINGB", "龙江银行"],["LZYH", "兰州银行"],["JSB", "晋商银行"],["BOHAIB", "渤海银行"],["YQCCB", "阳泉银行"],["SJBANK", "盛京银行"],["XABANK", "西安银行"],["BSB", "包商银行"],["JSBANK", "江苏银行"],["FSCB", "抚顺银行"],["XYBANK", "信阳银行"],["NBYZ", "鄞州银行"],["LSBC", "临商银行"],["BOCD", "承德银行"],["SDRCU", "山东农信"],["NCB", "南昌银行"],["TCCB", "天津银行"],["CDCB", "成都银行"],["HANABANK", "韩亚银行"],["LYBANK", "洛阳银行"],["ZBCB", "齐商银行"],["XTB", "邢台银行"],["SHBANK", "上海银行"],["JLBANK", "吉林银行"],["H3CB", "内蒙古银行"],["BZMD", "驻马店银行"],["SZSBK", "石嘴山银行"],["DZBANK", "德州银行"],["SRBANK", "上饶银行"],["CSCB", "长沙银行"],["JHBANK", "金华银行"],["BHB", "河北银行"],["BGB", "广西北部湾银行"],["NYNB", "广东南粤银行"],["JXBANK", "嘉兴银行"],["CCQTGB", "重庆三峡银行"],["ZZBANK", "郑州银行"],["SCCB", "三门峡银行"],["HRXJB", "华融湘江银行"],["BANKWF", "潍坊银行"],["FJHXBC", "福建海峡银行"],["ORBANK", "鄂尔多斯银行"],["XXBANK", "新乡银行"],["WHCCB", "威海市商业银行"],["KORLABANK", "库尔勒市商业银行"],["ZYCBANK", "遵义市商业银行"],["ZJKCCB", "张家口市商业银行"],["HBYCBANK", "湖北银行宜昌分行"],["HBHSBANK", "湖北银行黄石分行"],["SRCB", "深圳农村商业银行"],["SHRCB", "上海农村商业银行"],["SDEB", "顺德农商银行"],["WRCB", "无锡农村商业银行"],["NXRCU", "宁夏黄河农村商业银行"],["GRCB", "广州农商银行"],["TCRCB", "江苏太仓农村商业银行"],["DYCB", "德阳商业银行"],["YBCCB", "宜宾市商业银行"],["YDRCB", "尧都农商行"],["WHRCB", "武汉农村商业银行"],["TACCB", "泰安市商业银行"],["MTBANK", "浙江民泰商业银行"],["KSRB", "昆山农村商业银行"],["YXCCB", "玉溪市商业银行"],["DRCBCL", "东莞农村商业银行"],["CDRCB", "成都农商银行"],["TRCB", "天津农商银行"],["ZJTLCB", "浙江泰隆商业银行"],["GYCB", "贵阳市商业银行"],["CGNB", "南充市商业银行"],["CSRCB", "常熟农村商业银行"],["ZRCBANK", "张家港农村商业银行"],["CZCB", "浙江稠州商业银行"],["DYCCB", "东营市商业银行"],["BJRCB", "北京农村商业银行"],["ZGCCB", "自贡市商业银行"],["CBKF", "开封市商业银行"],["CRCBANK", "重庆农村商业银行"],["LSCCB", "乐山市商业银行"],["JZBANK", "晋中市商业银行"],["HZCCB", "湖州市商业银行"],["JRCB", "江苏江阴农村商业银行"],["LYCB", "辽阳市商业银行"],["WJRCB", "吴江农商银行"],["URMQCCB", "乌鲁木齐市商业银行"],["GZRCU", "贵州省农村信用社"],["HURCB", "湖北省农村信用社"],["SCRCU", "四川省农村信用"],["JSRCU", "江苏省农村信用联合社"],["GDRCC", "广东省农村信用社联合社"],["CZRCB", "常州农村信用联社"],["ZJNX", "浙江省农村信用社联合社"],["HNRCU", "河南省农村信用"],["HNRCC", "湖南省农村信用社"],["JXRCU", "江西省农村信用"],["NHB", "南海农村信用联社"],["YNRCC", "云南省农村信用社"],["GXRCU", "广西省农村信用"],["ARCU", "安徽省农村信用社"],["GSRCU", "甘肃省农村信用"],["HBRCU", "河北省农村信用社"],["JLRCU", "吉林农信"],["XLBANK", "中山小榄村镇银行"],["CDB", "国家开发银行"],["NHQS", "农信银清算中心"],["CBBQS", "城市商业银行资金清算中心"]]

oldlist = oldstr.split(',')
newlist = []

# 確認大發本身支持的銀行名稱
def checkBank(bankName:str):
    
    if (bankName == "中国工商银行"):
        bankName ="工商银行"
    elif(bankName == "中国建设银行"):
        bankName ="建设银行"
    elif(bankName =="中国民生银行"):
        bankName ="民生银行"
    elif(bankName =="中国招商银行"):
        bankName ="招商银行"
    elif(bankName =="中国交通银行"):
        bankName ="交通银行"
    elif(bankName =="浦东发展银行"):
        bankName ="浦发银行"
    elif(bankName =="上海浦东发展银行"):
        bankName ="浦发银行"
    elif(bankName =="广东发展银行"):
        bankName ="广发银行"
    elif(bankName =="中国光大银行"):
        bankName ="光大银行"
    elif(bankName =="中国邮政储蓄"):
        bankName ="邮政储蓄"
    elif(bankName =="中国邮政储蓄银行"):
        bankName ="邮政储蓄"
    elif(bankName =="中国农业银行"):
        bankName ="农业银行"
    return bankName

def printBankDic():
    resultStr=""
    bankList=[]
    for i in bankDic:
        ikey = bankDic[i]
        ikey = checkBank(ikey)
        # 銀行鍵值對
        bankKV = f"{ikey}-{i}"
        bankList.append(bankKV)
    
    resultStr = ",".join(bankList)
    return resultStr

#resultStr = printBankDic()


def printBankStr(change=False):
    resultStr=""
    
    for item in oldlist:
        ikey=""
        iVal=""
        ikeyV = item.split('-')
        if(change):
            ikey = ikeyV[1]
            iVal = ikeyV[0]
        else:
            ikey = ikeyV[0]
            iVal = ikeyV[1]
        ikey=checkBank(ikey)

        newlist.append(f"{ikey}-{iVal}")

    resultStr=",".join(newlist)
    return resultStr


def printBankList():
    resultStr=""
    newBankList = []
    for item in bankList:
        bankName = item[1]
        bankName = checkBank(bankName)
        bankCode = item[0]
        bankKv = f"{bankName}-{bankCode}"
        newBankList.append(bankKv)
    resultStr =",".join(newBankList)
    return resultStr

resultStr = printBankStr(True)

print(resultStr)



    