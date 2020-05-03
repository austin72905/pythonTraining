#載入模組module
#import sys
#print(sys.platform)
#載入自訂模組
import sys
sys.path.append("modules") #請他在當前的路徑下再多增加modules
import MasterMath

distance=MasterMath.Distance(0,0,3,4)
print(distance)
# import sys
# print(sys.path)
