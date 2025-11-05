a, b =map(int, input().split())

m = list(map(int, input().split()))
n = list(map(int, input().split()))
o = []
left = 0
right = 0
while left < a  and right<b:
        if m[left]< n[right] :
                o.append(m[left])
                left+=1
        else:
                o.append(n[right])
                right+=1
if left < len(m):
        o+=m[left:]
if right < len(n):
        o+=n[right:]
print(*o)        
                