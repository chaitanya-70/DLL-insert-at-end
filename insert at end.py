#Insert at End


class Node:
    def __init__(s,data):
        s.data=data
        s.prev=None
        s.next=None
class DLL:
    def __init__(s):
        s.head=None
    def iae(s,data):
        newnode=Node(data)
        if s.head is None:
            s.head=newnode
            return
        temp= s.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
    def display(s):
        temp=s.head
        print("Double Linked List:")
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
dll=DLL()
n=int(input("enter the no of elements to insert at end"))
for i in range(n):
    val=int(input(f"enter element {i+1}:"))
    dll.iae(val)
dll.display()







