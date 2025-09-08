s = []
for _ in range(int(input())):
        m, n = map(int, input().split())
        z = list(map(int, input().split()))
        y = sorted(z)
        ma = 1
        n_ma = 0
        if len(y) > 1:
                for i in range(1, len(y)):
                        if y[i] - y[i-1] <= n:
                                ma += 1
                        else:
                                if ma > n_ma:
                                        n_ma = ma
                                ma = 1
                if ma > n_ma:
                        n_ma = ma
                s.append(len(y)-n_ma)
        else:
              s.append(0)  
        
for i in s:
        print(i)
                             

