import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt_ajisai = 0  # counts diffs at odd indices (1-based)
    cnt_mai    = 0  # counts diffs at even indices (1-based)

    # i is 0-based here; index (i+1) is 1-based
    for i in range(n):
        if a[i] != b[i]:
            if (i + 1) % 2 == 1:   # (i+1) odd -> Ajisai controls
                cnt_ajisai += 1
            else:                  # (i+1) even -> Mai controls
                cnt_mai += 1

    if cnt_ajisai > cnt_mai:
        print("Ajisai")
    elif cnt_mai > cnt_ajisai:
        print("Mai")
    else:
        print("Tie")
