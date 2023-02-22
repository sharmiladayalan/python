#list
l=[10,'pooja',.78,True]
print(l)
print(l[0])
print(l[1])
print(l[2])
print(l[3])
#  0   1   2       3
s=[10,10,"pooja",'pooja']#list can accept a duplicate value
print(s[-1])
print(s[0:3:1])#10,10,"pooja",'pooja'
print(s[0:3:2])
print(type(s))
#list methods
#append()
 #  0 1 2 3 4 5 6 7 8
l=[1,2,3,4,5,6,7,8,9]
print(l[1:5])
print(l[1:5:1])
print(l[1:5:2])
print(l[1:5:3])
s=[10,10,'pooja','sharmila']
s.append(320)
print(s)
#string is immutable
#insert index,values
s.insert(1,'moolya')
print(s)
s.remove('pooja')
print(s)
