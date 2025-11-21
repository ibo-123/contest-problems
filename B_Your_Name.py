
from collections import Counter
for _ in range(int(input())):
        m = int(input())
        a , b = input().split()
        c = Counter(a)
        d = Counter(b)
        if c == d:
                print("YES")
        else:
                print("NO")