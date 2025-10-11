class Multiplay:
        def __init__(self):
                self.result=0
        def multi(self,a,b):
                self.result=a*b
                return self.result
p=Multiplay()
print(p.multi(5,4))