for _ in range(int(input())):
        y=int(input())
        z=list(map(int,input().split()))
        u,v=set(z)
        if z.count(u)>1:
                print(z.index(v)+1)
        else:
                print(z.index(u)+1)