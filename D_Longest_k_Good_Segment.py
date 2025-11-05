m , n = map(int,input().split())
lists = list(map(int,input().split()))

max_length = 0
left = 0
right = 0
indexs = [0 , 0]
while right < m:
        if len(set(lists[left : right + 1])) <= n:
                while len(set(lists[left : right + 1])) <= n and right < m:
                        right += 1
        else:
                max_length = max(max_length, right - left + 1)
                if max_length == right - left:
                        indexs = [left , right - 1]
                
        left +=1
if indexs[0] == indexs[1] == 0:
        indexs = [0 , 0+n-1]
        
print(indexs[0] + 1 , indexs[1] + 1)