for _ in range(int(input())):
        b = list(map(int,input().split()))
        if len(set(b)) == 1:
                print("YES")
        else:
                print("NO")