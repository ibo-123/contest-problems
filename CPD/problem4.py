for _ in[0]*int(input()):
 n,k=map(int,input().split())
 s=input()
 a=s[:k].count('W')
 mini=a
 for i in range(1,n-k+1):
  a+=(s[k+i-1]=='W')-(s[i-1]=='W')
  mini=min(mini,a)
 print(mini)