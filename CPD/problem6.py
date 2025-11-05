for _ in range(int(input())):
        y = int(input())
        l = list(map(int,input().split()))
        max_ = l[0]
        sum_ = 0
        left = l[0]//abs(l[0])
        for i in l[1:]:
                if left == (i//abs(i)):
                        if max_<i:
                                max_=i
                else:
                        sum_+=max_
                        max_ = i
                        left = i//abs(i)
        sum_+=max_
        print(sum_)
                        