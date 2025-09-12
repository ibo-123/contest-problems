for i in range(int(input())):
    y=int(input())
    if y%4==0:
        print('YES')
        even=0
        for j in range(int(y//2)):
            even+=2
            print(even,end=" ")
        odd=1
        l=y//4
        print(odd,end=" ") 
        for j in range(int(y//2)-1):
            if j==l-1:
               odd+=4
               print(odd,end=" ") 
            else:
                odd+=2
                print(odd,end=" ")
            print('')    
    else:
            print('NO')