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
            print(temp.data)
            temp = temp.next

    def removeDuplicate(self):
        temp = self.head
        while temp.next != None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
            
llist = linkedList()
llist.head = Node(1)
second = Node(1)
third = Node(3)
fourth = Node(4)
llist.head.next = second
second.next = third
third.next = fourth
fifth = Node(4)
sixth = Node(6)
fourth.next = fifth
fifth.next = sixth
print("With Duplicates")
llist.printList()
llist.removeDuplicate()
print("Without Duplicates")
llist.printList()

