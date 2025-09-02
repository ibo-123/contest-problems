x=input()
if int(x)<0:
        n=x[:-1]
        m=x[:-2]+x[-1]
        if int(n)<int(m):
                if int(m)<0:
                        print(m)
                else:
                        print(0)
        else:
            print(n)
else:
        print(x)