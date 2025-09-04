import sys
for _ in range(int(input())):
        n,m=map(int,input().split())
        z=list(map(int,input().split()))
        s=sum(z)
        o=s
        for j in range(m):
                n=0
                old=0
                start,end,num=map(int,input().split())
                for k in z[start-1:end]:
                        n+=1
                        old+=k
                new=n*num
                s=s-old+new 
                if s%2==1:
                        sys.stdout.write("YES\n")
                else:
                        sys.stdout.write("NO\n")
                s=o
                
                        