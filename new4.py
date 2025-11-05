
m , o = map(int, input().split())
p = list(map(int, input().split()))
n = [0]
new = [0]
for i in range(m-1):
        if p[i] < p[i+1]:
                n.append(0)
        else:
                n.append(p[i] - p[i+1])
for i in range(m-1):
        if p[i] > p[i+1]:
                new.append(0)
        else:
                new.append(p[i+1] - p[i])
prefix_sum = [0]*(len(n)+1)
prefix_new = [0]*(len(new)+1)
for i in range(1,len(new)+1):
        prefix_new[i] = prefix_new[i-1] + new[i-1]

for i in range(1,len(n)+1):
        prefix_sum[i] = prefix_sum[i-1] + n[i-1]
# print(new)
# print(prefix_sum)
# print(prefix_new)
for i in range(o):
        a , b = map(int, input().split())
        if b > a:
                sum_ = prefix_sum[b] - prefix_sum[a]
                print(sum_)
        else:
             sum_ = prefix_new[a] -prefix_new[b]
        
             print(sum_)
