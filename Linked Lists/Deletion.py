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

    #deletion at the beginning
    def deleteHead(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    #deleting at given position
    def deleteAtPos(self,pos):
        i = 0
        temp = self.head
        while i < pos - 2:
            temp = temp.next
            i += 1
        temp.next = temp.next.next

    #deleting given key
    def deleteKey(self,element):
        temp = self.head
        if temp is not None:           #if head node itself contains the data
            if temp.data == element:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == element:
                break
            prev = temp
            temp = temp.next

        if temp == None:             #if no such element exists
            return
        prev.next = temp.next
        temp = None   



    #deleting at end
    def deleteEnd(self):
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None
        


llist = linkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
llist.head.next = second
second.next = third
third.next = fourth
llist.printList()
print("After deleting the head node")
llist.deleteHead()
llist.printList()
fifth = Node(5)
sixth = Node(6)
fourth.next = fifth
fifth.next = sixth
llist.printList()
print("After deleting at given position")
ele = int(input("Enter position to delete:"))
llist.deleteAtPos(ele)
llist.printList()
llist.deleteEnd()
print("After deleting tail")
llist.printList()
key = int(input("Enter the key value to be deleted:"))
print("After deleting the given key")
llist.deleteKey(key)
llist.printList()