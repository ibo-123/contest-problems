x=int(input())
for i in range(x):
        y=int(input())
        m=0
        c=0
        while y>1:
                m+=1
                if y>2:
                        if y%6==0:
                                y//=6
                                c=0
                        else:
                                y*=2
                                c+=1
                elif y<1 or y==2:
                                m=-1
                                break
                if c>=2:
                        m=-1
                        break
                
               
        print(m)