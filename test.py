for i in range(int(input())):
    y=input()
    m=input()
    left = 0
    right = 0
    truth = False
    coun = 0
    while left < len(y) and right < len(m):
        if y[left] == m[right] and not truth and left == 0:
            truth = True
            coun+=2
        elif y[left] == m[right] and truth:
            coun+=1
        elif y[left] != m[right] and truth:
             coun +=2
             truth = False
        else:
            coun+=2
        left+=1
        right+=1
    coun+=len(y[left:]) + len(m[right:])
    print(coun)