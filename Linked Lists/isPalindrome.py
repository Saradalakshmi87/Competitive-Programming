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

    def isPalindrome(self):
        stack = []
        ispalin = True
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow
        while temp != None:
            stack.append(temp.data)
            temp = temp.next

        #print(stack)
        temp1 = self.head
        while stack:
            a = stack.pop()
            if a == temp1.data:
                ispalin = True
            else:
                ispalin = False
                break
            temp1 = temp1.next
        return ispalin

llist = linkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(3)
llist.head.next = second
second.next = third
third.next = fourth
fifth = Node(2)
sixth = Node(1)
fourth.next = fifth
fifth.next = sixth
llist.printList()
if llist.isPalindrome():
    print("Palindrome")
else:
    print("Not palindrome")
        
# This problem can also be done by reversing the linked list