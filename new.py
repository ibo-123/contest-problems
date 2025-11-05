import math
for i in range(int(input())):
        a,b = map(int,input().split())
        c,d = map(int,input().split())
        n = math.floor(math.log(a))
        m = math.floor(math.log(c))
        if n > m:
                print(">")
        elif m<n:
                print("<")
        else:
                k = [str(a)]
                s = [str(c)]
                for i in range()
                