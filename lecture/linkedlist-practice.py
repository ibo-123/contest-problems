class Node:
       def __init__(self , data):
              self.data = data
              self.next = None

def traversary_of_linked_list(head):
        current = head
        while current:
                print(current.data, end="->")
                current = current.next
        print('none')

def fond_the_lowes_node(head):
        min_val = head.data
        current = head.next
        
        while current:
                if current.data<min_val:
                        min_val = current.data
                current = current.next
        return min_val





node1 = Node(3)
node2 = Node(4)
node3 = Node(5)
node4 = Node(10)

node1.next = node2
node2.next = node3
node3.next = node4

#traversary_of_linked_list(node1)

#print(fond_the_lowes_node(node1))


def insert_node_at_position(head , new_node , position):
        if position == 1:
                new_node.next = head
                return new_node
        
        
        current = head
        
        for _ in range(position-2):
                if current is None:
                        break
                current = current.next
                
        new_node.next = current.next
        current.next = new_node
        return head

new_node = Node(50)

insert_node_at_position(node1 , new_node , 2)

traversary_of_linked_list(node1)



"""def delet_node(head, delete_node):
        if head == delet_node:
                return head.next
        current = head
        while current and current.next != delete_node:
                current = current.next
        if current is None or current.next is None:
                return head
        current.next = current.next.next
        return head
                
head = node1
head = delet_node(head,node1)

current = head
while current:
        print(current.data,end = "->")
        current = current.next
print("null")

new_node = Node(30)
new_node.next = head
head = new_node

current = head
while current:
        print(current.data,end = "->")
        current = current.next
print("null")

"""

   
""" 


       
class Node2:
        def __init__(self , data):
                self.data = data
                self.next = None
                self.prev = None
node1 = Node2(3)
node2 = Node2(4)
node3 = Node2(5)
node4 = Node2(10)

node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3


current = node4

while current.prev:
        print(current.data,end = "->")
        current = current.prev
print("null")
"""

