n,m=map(int,input().split())
total=0
new=1
while n>new:
        if new%m==0:
                n+=1
        new+=1
if new%m==0:
        n+=1
print(n)