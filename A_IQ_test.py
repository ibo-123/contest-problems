from collections import Counter

m = int(input())
a = list(map(int, input().split()))

d = Counter()
for i in range(len(a)):
        if a[i] % 2 == 0:
                d["even"] += 1
        elif a[i] % 2 == 1:
                d["odd"] += 1
if d["even"] > d["odd"]:
        for i in range(len(a)):
                if a[i] % 2 == 1:
                        print(i + 1)
                        break
else:
        for i in range(len(a)):
                if a[i] % 2 == 0:
                        print(i + 1)
                        break