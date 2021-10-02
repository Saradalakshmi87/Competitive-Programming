#Creating a NODE
class Node:
    def __init__(self,data):
        self.data = data                 #Assigns data
        self.next = None                 #Initializes next to NULL

class Linkedlist:
    def __init__(self):                  #Initializong head
        self.head = None
    def printList(self):                 #Printing Linked list (Traversal)
        temp = self.head                 
        while temp != None:
            print(temp.data)
            temp = temp.next

#Creating Linked list object 
llist = Linkedlist()
#Creating Nodes
llist.head = Node(1)
second = Node(2)
third = Node(3)
#Joining nodes through links
llist.head.next = second
second.next = third
llist.printList()
