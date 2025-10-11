for i in range(int(input())):
    y=input()
    truth=False
    if len(y)%2==0:
        right=len(y)//2-1
        left=len(y)-1
        while right>=0:
            if y[right]==y[left]:
                truth=True
            else:
                truth=False
                break
            right-=1
            left-=1
    if truth:
        print('YES')  
    else:
        print('NO')   