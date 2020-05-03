#定義類別和屬性
class IO:
  List_source=["console","file"]
  def read(src):
    if src not in IO.List_source:
      print("not sup")
    else:
      print("read from",src)
    

#使用類別
IO.read(IO.List_source[1])