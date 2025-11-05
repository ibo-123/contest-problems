for _ in range(int(input())):
        n =int(input())
        a = list(map(int,input().split()))
        m = [0]*(n+2)
        m[a[0]]+=1
        h = True
        for i in a[1:]:
                if m[i-1]==0 and m[i+1]==0:
                       h = False 
                       break
                m[i]+=1    
        if h:
             print("YES")
        else:
             print("NO")
                         
        
        