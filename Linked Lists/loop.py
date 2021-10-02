class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.flag = 0           #To check whether the particular node is visited or not

class linkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def detectLoop(self):
        temp = self.head
        while temp != None: 
            if temp.flag == 1:
                return "Loop detected"
            temp.flag = 1
            temp = temp.next
        return "No loop detected"

    '''
                  APPROACH - 2
        ---------------------------------
    def detectLoop(self):
        slow,fast = self.head,self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return "Loop detected"
        return "No loop detected"
    '''

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

'''seventh = Node(7)
sixth.next = seventh
seventh.next = fourth'''

print(llist.detectLoop())
#llist.printList()
            
