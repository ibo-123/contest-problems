for _ in range(int(input())):
        x,y=input().split()
        z,w=input().split()
        x=x+(int(y)*"0")
        z=z+(int(w)*"0")
        if int(x)>int(z):
                print(">")
        elif int(x)<int(z):
                print("<")
        else:
                print("=")