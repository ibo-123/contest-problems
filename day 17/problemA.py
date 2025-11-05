for _ in range(int(input())):
        y= input()
        if len(y)<=2:
                print("NO")
                continue
        n = y[:2]
        if int(n)!=10:
                print("NO")
                continue
        s = y[2:]
        if int(s[0]) == 0:
                print("NO")
                continue
        if int(s)<2:
                print("NO")
                continue
        print("YES")