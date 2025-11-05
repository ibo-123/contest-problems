for _ in range(int(input())):
        n = int(input())
        m = list(map(int,input().split()))
        if  len(set(m))>2:
                print("YES")
        else:
                if 1 in m:
                        if m.count(1)>len(m)//2:
                                print("NO")
                        else:
                                print("YES")
                elif n==1:
                                print("NO")
                else:
                        print("YES")
        