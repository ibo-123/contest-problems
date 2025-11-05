m , k = map(int,input().split())
sum_ = 0
i = 0

while i<=k:
        sum_ += ((m**i) * (i**m))
        if sum_ >= (10**9 + 7):
                sum_ %= (10**9)+7
                break
        i+=1
print(sum_)