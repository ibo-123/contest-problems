for _ in range(int(input())):
        n = int(input())
        m = list(map(int,input().split()))
        f = {}
        for j in m:
                if not f[j] in f:
                        f[j]=[m.index(j)]
                else:
                        f[j].append(m.index(j))
        
        for i in range(int(input())):
                y = input()
                o = {}
                if len(y)<n or len(set(y))<len(set(m)) or len(y)>n or len(set(y))>len(set(m)):
                        print("NO")
                        continue
                for j in y:
                    if not o[j]:
                        o[j]=[y.index(j)]
                    else:
                        o[j].append(y.index(j))
                if m == o:
                        print("YES")
                else:
                        print("NO")
                        
                