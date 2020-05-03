#距離 X平方+Y平方 開根號 = 兩點距離
def Distance(x1,y1,x2,y2):
  return ((x2-x1)**2+(y2-y1)**2)**0.5  #0.5次方就等於開根號

#斜率 y/x
def Slope(x1,y1,x2,y2):
  return (y2-y1)/(x2-x1)