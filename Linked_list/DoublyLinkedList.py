class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def InsertAtBegin(self, data):
        if self.head == None:
            self.head = Node(data, self.head, None)
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def printLL(self):
        itr = self.head
        
        while itr:
            print(f"{itr.data} --> ", end='')   
            itr = itr.next
        print()

    def printLLRev(self):
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        while itr:
            print(f"{itr.data} <-- ", end='')
            itr = itr.prev
        print()


if __name__ == '__main__':
    dll = DoublyLinkedList()
    
    dll.InsertAtBegin(3)
    dll.InsertAtBegin(2)
    dll.InsertAtBegin(1)
    
    dll.printLL()
    dll.printLLRev()
