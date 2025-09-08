z=input()
s=0
tr=True
f=0
n=""
while s<len(z):
      m=z[s]
      if n=="":
           if m=="1":
                   n+=m
           else:
                   tr=False
                   break
      elif n=="1":
              if m=="1":
                   n=""
                   n+=m
              elif m=="4":
                      n+=m
              else:
                   tr=False
                   break   
      elif n=="14":
              if m=="1":
                   n=""
                   n+=m
              elif m=="4":
                      n+=m
              else:
                   tr=False
                   break   
      elif n=="144":
              if m=="1":
                   n=""
                   n+=m
              else:
                   tr=False
                   break   
      #print(tr,s,n)
      s+=1
      
if tr:
        print("YES")
else:
        print("NO")