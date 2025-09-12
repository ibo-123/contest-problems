x=input()
left=0
right=1
coun=0
while right<len(x):
        if x[left]==x[right]:
                coun+=1
                right+=1
        else:
                coun=1
                left=right
                right=left+1
        if coun>=7:
                m="YES"
                break
        else:
                m="NO"
print(m)