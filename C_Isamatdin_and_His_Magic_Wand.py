for _ in range(int(input())):
        m = int(input())
        a = list(map(int,input().split()))
        truth_even = False
        truth_odd = False
        index =0 
        while index < m:
                if a[index] % 2 == 0:
                        truth_even = True
                elif a[index] % 2 != 0:
                        truth_odd = True
                index+=1
        if truth_odd and truth_even:
                print(*(sorted(a)))
        else:
                print(*a)