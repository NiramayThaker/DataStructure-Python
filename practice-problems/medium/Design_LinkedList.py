class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class MyLinkedList:

    def __init__(self):

        self.head = Node(0)
        self.length = 0

    def get(self, index: int) -> int:
        
        if index < 0 or index >= self.length:
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.data

    def addAtHead(self, data: int) -> None:
        self.addAtIndex(0, data)

    def addAtTail(self, data: int) -> None:
        self.addAtIndex(self.length, data)

    def addAtIndex(self, index: int, data: int) -> None:
       
        if index > self.length:
            return
       
        if index < 0:
            index = 0
            
        self.length += 1
        pred = self.head
        
        for _ in range(index):
            pred = pred.next
            
        to_add = Node(data)
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        
        if index < 0 or index >= self.length:
            return
        
        self.length -= 1
        pred = self.head
        
        for _ in range(index):
            pred = pred.next
            
        pred.next = pred.next.next


