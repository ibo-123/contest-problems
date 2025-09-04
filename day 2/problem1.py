x=int(input())
y=input()
f=y[0]+y[1]
m={f:1}
for i in y[2:]:
        f=f[1]+i
        if f in m :
                        m[f]+=1
        else:
                m[f]=1
mn=0
ms=""      
for i,j in m.items():
     if mn<j:
             ms=i
             mn=j
print(ms)   
        