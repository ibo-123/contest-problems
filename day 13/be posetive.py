for _ in range(int(input())):
        m=int(input())
        a=map(int,input().split())
        coun=0
        n=0
        for i in a:
                if i==-1:
                        n+=1
                elif i==0:
                        coun+=1
        if n>0 and n%2==1:
                        coun+=2
        print(coun)