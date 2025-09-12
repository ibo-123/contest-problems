n=[]
for _ in range(int(input())):
        row,col=map(int,input().split())
        m=""
        for j in range(row):
                y=input()
                m+=y
        c=m.count("#")//2+1
        
        s=1
        while c:
                if m[s-1]=="#":
                        c-=1
                o=s
                s+=1
        rows=(o)//col+1
        cols=(o)%col
        if len(m)==1:
                cols+=1
                rows-=1
        n.append([rows,cols])
for i,j in n:
      print(i,j)              