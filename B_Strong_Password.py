n = int(input())
m = [0]*(n+1)
s = []
for _ in range(int(input())):
        l,k,o = map(int,input().split())
        m[l-1]+=o
        m[k]-=o
        # s.append((l,k,o))
for i in range(1,n):
        m[i]+=m[i-1]
# """for i in range(len(s)):
#         m[s[i][0]]+=s[i][2]
#         m[s[i][1]]-=s[i][2]"""
        
print(*m[:-1])

"""
5 3         arr[] size n = 5, queries[] size q = 3
1 2 100     queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
2 5 100
3 4 100
        """

"""
a b k
    1 5 3
    4 8 7
    6 9 1
"""