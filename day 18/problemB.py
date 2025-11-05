for _ in range(int(input())):
        y = int(input())
        m = list(map(int , input().split()))
        coun = 0
        occure = 0
        num = m[0]
        truth = False
        fine  = True
        for i in m:
                if num == i:
                        coun+=1
                elif not truth :
                        occure = coun
                        truth = True
                        num = i
                        coun = 1
                else:
                        if coun > occure or coun <occure :
                                fine = False
                                break
                        num = i
                        coun = 1
                if fine:
                        print("YES")
                else:
                        print("NO")