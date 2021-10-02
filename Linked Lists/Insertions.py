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
            print(temp.data,end = " ")
            temp = temp.next
        print()
    
    #Insertion at the beginning
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    
    #Insertion at given position
    def InsertPos(self,pos,new_data):
        temp = self.head
        new_node = Node(new_data)
        i = 0
        while i < pos - 1:
            temp = temp.next
            i += 1
        new_node.next = temp.next
        temp.next = new_node


    #Insertion at the end
    def InsertAtEnd(self,new_data):
        temp = self.head
        new_node = Node(new_data)
        while temp.next != None:
            temp = temp.next
        temp.next = new_node


#Creating Linked list object 
llist = Linkedlist()
#Creating Nodes
llist.head = Node(1)
second = Node(2)
third = Node(3)
#Joining nodes through links
llist.head.next = second
second.next = third
print("Before")
llist.printList()
llist.push(4)
print("After")
llist.printList()
llist.InsertPos(2,5)
print("After Inserting at given position")
llist.printList()
llist.InsertAtEnd(6)
print("After inserting at end")
llist.printList()
