a , b = map(int, input().split())
n = list(map(int, input().split()))

l = sorted(n)
l = l[::-1]
prefix_sum = [0]*(a+1)
for i in range(1,a+1):
    prefix_sum[i] = prefix_sum[i-1] + l[i-1]
for i in range(b):
    c , d  = map(int, input().split())
    minm = c - d
    d+=minm
    print(prefix_sum[d] - prefix_sum[minm])