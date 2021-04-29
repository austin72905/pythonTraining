a = [1,2,3]
b = [2,3,4,5]
inter = [i for i in a if i  in b ]
print(inter)

a = [1, 2, 3, 4, 5]
b = [3, 4, 5]
d = [False for c in b if c not in a]
print(d)
if d:
    print ("a不包含b的所有元素")
else:
    print ("a包含b的所有元素")