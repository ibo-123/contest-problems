for _ in range(int(input())):
        x = int(input())
        l = list(map(int,input().split()))
        s = 0
        m = 0
        bulb = False
        for i in l:
                s+=abs(i)
                if i<0 and not bulb:
                        bulb=True
                        m+=1
                elif i>0 and bulb:
                        bulb = False
        print(s, m)
                        
                        
        