for _ in range(int(input())):
        a,b=map(int,input().split())
        z=list(map(int,input().split()))
        n=z.index(max(z))
        if sorted(z)==z and len(set(z))==len(z):
                print(a-z[-1]+1)
        else:
                print(1)