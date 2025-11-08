for _ in range(int(input())):
        m , n = map(int, input().split())
        p = list(map(int, input().split()))
        prefix_sum = [0]*(m+1)
        for i in range(1,m+1):
                prefix_sum[i] = prefix_sum[i-1] + p[i-1]
        for i in range(n):
                a , b , c = map(int, input().split())
                sum_ = prefix_sum[b] - prefix_sum[a-1]
                added = c * (b - a + 1) - sum_
                final = added + prefix_sum[m]
                if final % 2 != 0:
                        print("YES")
                else:
                        print("NO")