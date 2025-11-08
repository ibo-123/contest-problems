import math


for i in range(int(input())):
        p , q = map(int , input().split())
        nums = list(map(int , input().split()))
        prev = nums[-1] - nums[-2] if len(nums) > 1 else nums[-1]
        bublb = True
        for i in range(len(nums)-2,0,-1):
                number = nums[i] - nums[i -1]
                if number <= prev :
                        prev = number
                else:
                        bublb = False
                        break
        if not  bublb:
                print("No")
        else:
                target = p - q + 1
                value = math.ceil(nums[0]/target )
                if value <= prev:
                        print("Yes")
                else:
                        print("No")
                
                        
        