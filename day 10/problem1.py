for _ in range(int(input())):
        y=int(input())
        a=list(map(int,input().split()))
        if sum(a)%2==0:
                two=a.count(2)
                one=a.count(1)
                if two%2==0 or (one%2==0 and one>=1):
                        print("YES")
                else:
                        print("NO")
        else:
                print("NO")
                        
