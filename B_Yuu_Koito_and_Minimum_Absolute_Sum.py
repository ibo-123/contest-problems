import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Extract endpoints
    first = a[0]
    last = a[-1]

    # Case: both known
    if first != -1 and last != -1:
        ans = abs(last - first)

    # Case: first unknown
    elif first == -1 and last != -1:
        first = last
        a[0] = first
        ans = 0

    # Case: last unknown
    elif first != -1 and last == -1:
        last = first
        a[-1] = last
        ans = 0

    # Case: both unknown
    else:
        first = 0
        last = 0
        a[0] = 0
        a[-1] = 0
        ans = 0

    # Fill all remaining -1 with 0
    for i in range(n):
        if a[i] == -1:
            a[i] = 0

    print(ans)
    print(*a)
