for _ in range(int(input())):
        y = int(input())
        l = input()
        coun = 0
        pos = False
        str = list(set(l))
        for char in str:
            current = 0
            left = 0
            right = len(l)-1
            curn = True
            while left < right:
                if l[left] == l[right] :
                        left+=1
                        right-=1
                elif l[left] == char:
                        left+=1
                        current+=1
                elif l[right]!= char:
                        right-=1
                        current+=1
                else:
                        curn = False
                        break
        if curn :
                pos = True
                coun = min(coun,current)
        if pos :
                print(coun)
        else:
                print(-1)
                
                