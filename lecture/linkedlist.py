class Node:
        def __init__(self,data):
               self.data=data
               self.next=None
class Linkedlist:
        def __init__(self):
                self.head=None
        def append(self,data):
                 new_node=Node(data)
                 if not self.head:
                         self.head=new_node
                         return
                 temp=self.head
                 while temp.next:
                         temp=temp.next
                 temp.next=new_node
        def display(self):
                nodes=[]
                temp=self.head
                while temp:
                        nodes.append(str(temp.data))
                        temp=temp.next
                print("->".join(nodes))
                
ll = Linkedlist()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display() 