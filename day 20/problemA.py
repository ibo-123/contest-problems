for _ in range(int(input())):
        a,b,c,d = map(int,input().split())
        c-=a
        d-=b
        n = True
        if a>b :
               if a%2== 0:
                       s = a//2 -1
               else:
                       s = a//2
               if b< s: 
                        n = False
        elif a<b:
               if b%2== 0:
                       s = b//2 -1
               else:
                       s = b//2
               if a< s: 
                        n = False
        if c>d :
               if c%2== 0:
                       s = c//2 -1
               else:
                       s = c//2
               if d< s: 
                        n = False
        elif c<d:
                if d%2== 0:
                       s = d//2 -1
                else:
                       s = d//2
                if c< s: 
                        n = False
        if n :
                print("YES")
        else:
                print("NO")