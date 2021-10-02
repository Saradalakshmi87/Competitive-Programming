class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    #Printing List
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data,end = " ")
            temp = temp.next
        print()

    #printing Nth Node
    def printNthNode(self,idx):
        c = 0
        temp = self.head
        while c != idx:
            temp = temp.next
            c += 1
        return temp.data

llist = linkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
llist.head.next = second
second.next = third
third.next = fourth
fifth = Node(5)
sixth = Node(6)
fourth.next = fifth
fifth.next = sixth
llist.printList()
index = int(input("Enter node index:"))
print("Nth node is: ",llist.printNthNode(index))