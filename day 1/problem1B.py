n,m=map(int,input().split())
if ((n%2==0 and m%2==0) or (n%2==0 and m%2==1) or (n%2==1 and m%2==0)) and (n!=1 and m!=1):
        print("Malvika")
else:
        print("Akshat")
