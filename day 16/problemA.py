for _ in range(int(input())):
        y=int(input())
        z=sorted(list(map(int,input().split())))
        m={}
        for i in range(0,y-1,2):
                m[z[i+1]-z[i]]=1
        print(max(m))