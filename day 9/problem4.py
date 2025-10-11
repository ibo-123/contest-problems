for _ in range(int(input())):
        m,n=map(int,input().split())
        a=list(map(int,input().split()))
        if n in a:
                print("YES")
        else:
                print("NO")