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

    def reverse(self,head,k):
        if head == None:
            return None
        prev = None
        curr = head
        cnt = 0
        next = None
        while(curr is not None and cnt < k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            cnt += 1

        if next is not None:
            head.next = self.reverse(next,k)

        return prev

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
k = int(input("Enter value of K : "))
llist.head = llist.reverse(llist.head, k)
llist.printList()