m,n = map(int,input().split())
l = list(map(int,input().split()))
sum_ = sum(l[:n])
left = 0
right = n-1
min_ = sum_
b = 0
while right < m:
        sum_ = sum_ + l[right] - l[left]
        if sum_ < min_:
                min_ = sum_
                b = left+1
                
        right+=1
        left+=1
print(b)