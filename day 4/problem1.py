k=int(input())
month=list(map(int,input().split()))
if sum(month)>=k:
        s=0
        coun=0
        if sum(month)==k:
                while 0 in month:
                       month.remove(0) 
                print(len(month))
        else:
           for i in range(len(month)):
                n=max(month)
                if s<k:
                        s+=n
                        coun+=1
                        month.remove(n)
                else: 
                        print(coun)
                        break
else:
        print(-1)