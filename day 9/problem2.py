for _ in range(int(input())):
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        coun=1
        p=1
        truth=True
        while coun<len(a):
                if [coun]<[coun-1]:
                        p+=1
                else:
                     if p>k:
                             truth=False
                             p=1
                     else:
                             p=1
      if truth:
              print("YES")
      else:
              print("NO")
                        