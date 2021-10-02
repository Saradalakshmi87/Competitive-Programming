class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data,end = " ")
            temp = temp.next
        print()

    def pairwiseSwap(self):
        temp = self.head
        if temp == None:
            return
        while temp and temp.next:
            if temp.data != temp.next.data:
                temp.data,temp.next.data = temp.next.data,temp.data

            temp = temp.next.next

llist = linkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
llist.head.next = second
second.next = third
third.next = fourth
fifth = Node(5)
#sixth = Node(6)
fourth.next = fifth
#fifth.next = sixth
print("Before swap")
llist.printList()
print("After swap")
llist.pairwiseSwap()
llist.printList()