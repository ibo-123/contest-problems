import math

for _ in range(int(input())):
        a, b = map(int, input().split())
        lcm =a*b// math.gcd(a, b)
        
        if a == b:
                print(0)
        elif lcm == a or lcm == b:
                print(1)
        else:
                print(2)