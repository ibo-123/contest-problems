x=int(input())
s=0
n=1
m=0
coun=0
while x>m:
       s+=n
       n+=1
       m+=s
       coun+=1
if m==x:
        print(coun)
else:
        print(coun-1)