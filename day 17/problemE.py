n = int(input())
v = list(map(int, input().split()))
p = [0]*(n+1)

for i in range(1,n+1):
        p[i] = p[i-1] + v[i-1]
v = sorted(v) 
o = [0]*(n+1)
for i in range(1,n+1):
        o[i] = o[i-1] + v[i-1]           

m = int(input())
for _ in range(m):
    type_, l, r = map(int, input().split())
    if type_ == 1:
            print(p[r]-p[l-1])
    else:
            print(o[r]-o[l-1])