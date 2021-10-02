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

    #APPROACH - 1
    '''
    Calculate the length of the linked list and do "LENGTH - N + 1", which results in the position of the node from the front
    '''
    def NthNodeFromLast(self,n):
        temp = self.head
        length = 0
        while temp != None:
            length += 1
            temp = temp.next
        i = 0
        temp = self.head
        if n > length:
            return "Beyond limit"
        while i < length - n:
            temp = temp.next
            i += 1
        return temp.data

    #APPROACH - 2    ------>   Two - pointer method
    '''
    1. Take 2 pointers (main ptr and ref ptr) that are pointing to the head initially.
    2. Move the ref ptr for "n" times using one loop.
    3. Run another loop till the "ref ptr" reaches last node... Parallely move the "main ptr". Whenever the ref ptr encounter None and
       at that point return the node that is pointing by main ptr.
    '''
    def NthNodeFromEnd(self,val):
        m_ptr  = self.head
        ref_ptr = self.head
        temp = self.head
        length = 0
        while temp != None:
            length += 1
            temp = temp.next
        if val > length:
            return "Beyond limit"
        i =0
        while i != val:
            ref_ptr = ref_ptr.next
            i += 1
        while ref_ptr != None:
            ref_ptr = ref_ptr.next
            m_ptr = m_ptr.next
        return m_ptr.data

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
n = int(input("Enter the node number from end: "))
print(llist.NthNodeFromLast(n))
val = int(input("Enter node position value:"))
print(llist.NthNodeFromEnd(val))  