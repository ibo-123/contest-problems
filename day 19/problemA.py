for _ in range(int(input())):
        a,b = map(int , input().split())
        a**=2
        b*=a
        print(b)