for _ in range(int(input())):
        n = int(input())
        m = n%3
        s = 3-m if m !=0 else 0
        print(s)