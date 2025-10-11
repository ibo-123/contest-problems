for _ in range(int(input())):
        y=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        minn=0
        for i in range(y):
                if a[i]>b[i]:
                        minn+=(a[i]-b[i])
                
        
        print(minn+1)       