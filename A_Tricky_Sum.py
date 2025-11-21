for _ in range(int(input())):
        n = int(input())
        m = n*(n+1)//2
        p = 1
        while p <= n:
                m-= 2*p
                p *= 2
        print(m)