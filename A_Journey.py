for _ in range(int(input())):
        n , a , b , c = map(int , input().split())
        m = n//(a+b+c)
        s = n - m*(a+b+c)
        coun = m*3
        if s > 0:
                s-=a
                coun+=1
        if s > 0:
                s-=b
                coun+=1
        if s > 0:
                s-=c
                coun+=1
        print(coun) 