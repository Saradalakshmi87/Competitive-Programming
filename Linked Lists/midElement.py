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

    '''
    #APPROACH - 1

    1. Find the length of the linked list.
    2. If length is odd, return data at length//2, otherwise return the data at length//2 and length//2 + 1

    #APPROACH - 2

    SLOW and FAST Pointers method
    -----------------------------
    1. Initialize head node to slow and fast pointers.
    2. Move one pointer by one and the other pointers by two. 
       When the fast pointer reaches the end slow pointer will reach the middle of the linked list.
    3. Return slow pointer

    #APPROACH - 3

    1. Initialize head node to mid and counter to 0.
    2. Traverse through the linked list and increment the counter variable by 1.
    3. Whenever the counter variable is odd, make mid to mid.next.
    4. Return the mid value if counter reaches length.

    '''
    def midEle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

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
llist.printList()
print("Mid element:",llist.midEle())