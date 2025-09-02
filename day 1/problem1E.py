x=int(input())
for i in range(x):
        y=int(input())
        if y>=2020:
                m=y//2020
                n=y%2020
                if n>0:
                        if m>=n:
                                s="YES"
                        else:
                                s="NO"
                else:
                        s="YES"
        else:
                s="NO"
        print(s)