a , b , c = map(int, input().split())
mi = min(a, b, c)
ma = max(a, b, c)
b = sorted([a, b, c])
if ma - mi >= 10:
        print("check again")
else:
        print(f"final {b[1]}")