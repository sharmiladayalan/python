s={10,30,50,50,60,70,'A'}
print(s)
print(len(s))
print(s)
print(50 in s)
s.add(100)
print(s)
s.pop()
print(s)
t={55,75,82,90,15}
s1={50,15,90,12}
z=t.union(s1)
print(z)
b=t.symmetric_difference(s1)
print(b)
c={55,75}
print(c.issubset(t))
c1={55,57}
print(c1.issubset(t))
c2={}
print(c2.issubset(t))
c.discard(57)
print(c)

